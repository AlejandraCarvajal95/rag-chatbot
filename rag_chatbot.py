from together import Together
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.together import TogetherLLM
import os

# Configurar embeddings locales
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

def main():
    load_dotenv()  # variables de entorno
    
    # Cargar documentos
    documents = SimpleDirectoryReader("data").load_data()
    print("Documentos cargados:")
    for doc in documents:
        print("→", doc.text[:200], "...")
    
    # Crear índice vectorial
    index = VectorStoreIndex.from_documents(documents)
    print("\nÍndice vectorial creado exitosamente!")
    
    # Crear motor de consulta
    query_engine = index.as_query_engine(
        llm=TogetherLLM(
            model="deepseek-ai/DeepSeek-V3",
            temperature=0.3,
            max_tokens=200,
            top_p=0.9,
            frequency_penalty=0.1,
            presence_penalty=0.1
        )
    )
    
    # Ejemplo de consulta RAG

    while True:
      user_input = input("\n Pregunta (o escribe 'salir'): ")
      if user_input.lower() in ["salir", "exit"]:
          break
    response = query_engine.query(user_input)
    print(f"\n respuesta: {response}")

    
    # Ejemplo con Together AI directo (sin RAG)
    print("\n" + "="*50)
    print("Ejemplo con Together AI directo:")
    
    client = Together()
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[
            {
                "role": "user",
                "content": "Dame 3 consejos breves para programar en Python"
            }
        ],
        temperature=0.5,
        max_tokens=100,
        top_p=0.9,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()