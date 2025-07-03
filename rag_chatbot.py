
from dotenv import load_dotenv  
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings  
from llama_index.embeddings.huggingface import HuggingFaceEmbedding  
from llama_index.llms.together import TogetherLLM  
import os
import pandas as pd  

# Configuración del modelo de embeddings para vectorización
# Intenta cargar un modelo local de HuggingFace para mayor velocidad
try:
    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
except Exception as e:
    print(f"Error cargando embeddings: {e}")
    # Fallback a OpenAI embeddings si falla el modelo local
    from llama_index.embeddings.openai import OpenAIEmbedding
    Settings.embed_model = OpenAIEmbedding()

def main():
    load_dotenv()

    documents = SimpleDirectoryReader("data").load_data()
    
    # Crear índice vectorial para búsqueda semántica eficiente
    index = VectorStoreIndex.from_documents(documents)

    # Configurar el motor de consulta RAG con parámetros optimizados
    query_engine = index.as_query_engine(
        # Configuración del modelo de lenguaje (Together AI)
        llm=TogetherLLM(
            model="deepseek-ai/DeepSeek-V3",  
            temperature=0.3,                  # Controla creatividad (0.1-1.0, menor = más preciso)
            max_tokens=100,                   # Máximo de tokens por respuesta
            top_p=0.9,                        # Controla diversidad de respuestas (0.8-0.95)
            frequency_penalty=0.1,            # Reduce repetición de palabras
            presence_penalty=0.1              # Fomenta uso de palabras nuevas
        ),
        response_mode="compact",              # Genera respuestas concisas y completas
        streaming=False,                      # Respuesta completa de una vez (no streaming)
        similarity_top_k=2,                   # Considera solo los 2 documentos más relevantes
        node_postprocessors=None              # Sin filtros adicionales que puedan cortar
    )

    # Simulación de integración con CRM - Saludo personalizado
    try:
        # Leer datos del cliente desde archivo CSV (simulación de CRM)
        df = pd.read_csv("clientes.csv")
        nombre = df.iloc[0]["nombre"]  # Obtener nombre del primer cliente
        mensaje = f"Redacta un saludo de bienvenida para el cliente {nombre}."
        response = query_engine.query(mensaje)  # Generar saludo personalizado con RAG
        print(f"\n{response}")
    except FileNotFoundError:
        print("\n⚠️  Archivo clientes.csv no encontrado. Usando saludo genérico.")
        print("¡Bienvenid@ a Servicios de Tecnología S.A.!")
    except Exception as e:
        print(f"\n⚠️  Error al leer datos del CRM: {e}")
        print("¡Bienvenid@ a Servicios de Tecnología S.A.!")

    # Bucle principal del chatbot - Interacción con el usuario
    while True:
        user_input = input("\n Pregunta (o escribe 'salir'): ")
        if user_input.lower() in ["salir", "exit"]:
            break
        try:
            # Procesar consulta del usuario usando RAG
            response = query_engine.query(user_input)
            print(f"\n respuesta: {response}")
        except Exception as e:
            # Manejo de errores para evitar que el programa se cierre
            print(f"\n❌ Error al procesar la consulta: {e}")
            print("💡 Intenta reformular tu pregunta o verifica tu conexión a internet.")

if __name__ == "__main__":
    main()
