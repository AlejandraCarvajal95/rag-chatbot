# 🧠 RAG Chatbot con LlamaIndex + Together.ai

Este demo muestra cómo construir un chatbot RAG (Retrieval-Augmented Generation) que indexa documentos empresariales y responde preguntas en lenguaje natural. Utiliza `LlamaIndex` para la recuperación semántica y `Together.ai` como backend LLM (modelo `DeepSeek-V3`). También incluye una simulación de integración con un CRM externo usando un archivo `clientes.csv`.

---

## 📁 Estructura del proyecto

├── data/
│ └── data.txt # Documento de referencia indexado
├── clientes.csv # Simula una fuente externa tipo CRM
├── rag_chatbot.py # Chatbot con RAG + integración externa
├── direct_llm_example.py # Consulta directa al modelo LLM sin RAG
├── .env # Contiene TOGETHER_API_KEY
├── requirements.txt
└── README.md

---

## 🚀 Tecnologías utilizadas

- **Python 3.10+**
- **LlamaIndex**
- **Together.ai (modelo: DeepSeek-V3)**
- **Embeddings locales (MiniLM-L6-v2)**
- **Pandas** (para lectura de CSV simulando CRM)
- **dotenv** (manejo de variables de entorno)

---

## 🛠️ Cómo ejecutar

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/rag-chatbot-demo.git
cd rag-chatbot-demo
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Crea un archivo .env con tu API Key de Together:
```bash
TOGETHER_API_KEY=sk-xxxxxxxxxxxxxxxxx
```

4. Ejecuta el chatbot RAG:
```bash
python rag_chatbot.py
```

5. (Opcional) Ejecuta una consulta directa al modelo (sin RAG):
```bash
python direct_llm_example.py
```
