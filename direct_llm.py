from together import Together
from dotenv import load_dotenv
import os

# Ejemplo de uso directo del modelo sin RAG (comparar flujo)
# Este archivo demuestra cómo usar Together AI directamente sin procesamiento RAG


def main():
    load_dotenv()

    client = Together()
    
    
    # Sin procesamiento RAG, el modelo responde solo con su conocimiento base
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",  
        messages=[
            {
                "role": "user",  # Rol del mensaje (usuario que hace la pregunta)
                "content": "Dame 2 consejos breves para programar en Python"  
            }
        ],
       
        temperature=0.5,                  # Controla creatividad (0.1-1.0, 0.5 = balanceado)
        max_tokens=200,                   # Máximo de tokens en la respuesta
        top_p=0.9,                        # Controla diversidad de respuestas (0.8-0.95)
        frequency_penalty=0.1,            # Reduce repetición de palabras frecuentes
        presence_penalty=0.1              # Fomenta uso de palabras nuevas y variadas
    )
    
    # Mostrar la respuesta del modelo
    # Extrae el contenido del primer mensaje de respuesta
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
