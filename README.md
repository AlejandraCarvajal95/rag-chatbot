# 🧠 RAG Chatbot with LlamaIndex + Together.ai

This demo showcases how to build a Retrieval-Augmented Generation (RAG) chatbot capable of indexing enterprise documents and answering natural language questions. It uses `LlamaIndex` or semantic document retrieval and `Together.ai` ( `DeepSeek-V3`) as the LLM backend. The project also includes a simulated CRM integration using a `clientes.csv` file to demonstrate how external business data can be incorporated into the chatbot..

---

## 📁 Project Structure

```bash
├── data/
│ └── data.txt # Reference document indexed by the chatbot
├── clientes.csv # Simulated external CRM data source
├── rag_chatbot.py # RAG chatbot with CRM integration
├── direct_llm_example.py # Direct interaction with the LLM (without RAG)
├── .env  # Stores the TOGETHER_API_KEY
├── requirements.txt
└── README.md
```
---

## 🚀 Technologies used

- **Python 3.10+**
- **LlamaIndex**
- **Together.ai (DeepSeek-V3)**
- **Sentence Transformers (MiniLM-L6-v2 local embeddings)**
- **Pandas** (CRM data simulation)
- **dotenv** (environment variable management)

---

## ✨ Features
- Retrieval-Augmented Generation (RAG)
- Semantic document search with LlamaIndex
- DeepSeek-V3 inference through Together AI
- Local embeddings using MiniLM-L6-v2
- Simulated CRM integration via CSV files
- Modular and easy-to-extend project structure

---

## 🛠️ Getting Started

1. Clone the repository:
```bash
git clone https://github.com/tuusuario/rag-chatbot-demo.git
cd rag-chatbot-demo
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file:
```bash
TOGETHER_API_KEY=sk-xxxxxxxxxxxxxxxxx
```

4. Run the RAG chatbot:
```bash
python rag_chatbot.py
```

5. (Optional) Run a direct LLM query without RAG:
```bash
python direct_llm_example.py
```

📫 Contact
Developed by María Alejandra Moya Carvajal

📧 lisindit@gmail.com
