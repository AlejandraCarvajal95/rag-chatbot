# RAG Chatbot con LlamaIndex + Together.ai

Este demo carga un archivo `.txt` con servicios empresariales, lo indexa con LlamaIndex, y permite hacer consultas en lenguaje natural usando el modelo `DeepSeek-V3` desde Together.ai.

## Tecnologías usadas
- Python
- LlamaIndex
- TogetherLLM
- Embeddings locales (bge-base-en-v1.5)

## Cómo ejecutar
1. Clona el repo
2. Agrega tu archivo `.env` con `TOGETHER_API_KEY=...`
3. Ejecuta `python rag_chatbot.py`
