
# 🎯 NVIDIA-Powered RAG Chatbot

This is a **Retrieval-Augmented Generation (RAG) chatbot** powered by NVIDIA's AI endpoints using LangChain. It uses ChromaDB for context retrieval and provides intelligent, contextual responses based on your custom data.

---

## 📦 **Project Setup Instructions**

### 🔧 **1. Clone the Repository**

```bash
git clone https://github.com/your-username/nvidia-rag-chatbot.git
cd nvidia-rag-chatbot
```

---

### 🐍 **2. Set Up a Python Virtual Environment**

Using a virtual environment ensures dependencies remain isolated.

#### ✅ **Create Virtual Environment**

```bash
python3 -m venv venv
```

#### ✅ **Activate Virtual Environment**

- **On macOS/Linux:**

```bash
source venv/bin/activate
```

- **On Windows:**

```bash
.env\Scripts\activate
```

#### ❌ **Deactivate Virtual Environment**

Once you're done working:

```bash
deactivate
```

---

### 📥 **3. Install Project Dependencies**

All required libraries are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

### 🔑 **4. Set Up Environment Variables**

Create a `.env` file in the root directory of the project and add your **NVIDIA API Key**:

```
NVIDIA_API_KEY=your_actual_api_key_here
```

---

### 🏃 **5. Running the RAG Chatbot**

To run the chatbot, simply execute:

```bash
python rag_chatbot.py
```

The chatbot will:
1. Load and embed text from `data.txt`.
2. Store embeddings in ChromaDB.
3. Answer your questions with context-aware responses using NVIDIA's AI models.

---

### 🛑 **6. Force Rebuild ChromaDB (Optional)**

If you want to clear and rebuild the ChromaDB vector store from scratch, simply delete the database folder before running:

```bash
rm -rf ./chroma_db  # For Linux/Mac
rd /s /q chroma_db  # For Windows (in Command Prompt)
```

---

### 📝 **7. Project Structure**

```
nvidia-rag-chatbot/
│
├── venv/                  # Python virtual environment
├── .env                   # Environment variables (ignored by Git)
├── chroma_db/             # ChromaDB vector database (ignored by Git)
├── data.txt               # Source data for embeddings
├── rag_chatbot.py         # Main chatbot application
├── requirements.txt       # Python dependencies
├── run.sh                 # Shell script to run the bot
└── README.md              # Project documentation
```

---

### 📚 **8. Sample Usage**

```bash
You: What is FAISS?

🔍 Retrieved 3 relevant documents from ChromaDB:
📄 Document 1: FAISS is a library for efficient similarity search and clustering of dense vectors.
📄 Document 2: Developed by Facebook AI Research, FAISS enables fast nearest neighbor search.
📄 Document 3: It is commonly used for machine learning applications such as vector search.

🤖 NVIDIA AI Response:
FAISS is an open-source library developed by Facebook AI Research that facilitates efficient similarity search and clustering of dense vectors, widely used in machine learning applications.
```

---

### ❓ **9. Troubleshooting**

- **Permission Errors (SQLite):**  
  Run the following command to ensure proper permissions:
  ```bash
  chmod -R u+w ./chroma_db
  ```

- **API Key Error:**  
  Make sure your `.env` file contains the correct NVIDIA API Key.

- **Virtual Environment Issues:**  
  Recreate the virtual environment:
  ```bash
  rm -rf venv
  python3 -m venv venv
  source venv/bin/activate
  ```

---

### 🙌 **10. Contributing**

Feel free to fork the project, open issues, and submit pull requests.

---

### ⚖️ **11. License**

This project is licensed under the [MIT License](LICENSE).

---

### 🚀 **12. Acknowledgments**

- [NVIDIA AI Endpoints](https://build.nvidia.com/)
- [LangChain](https://docs.langchain.com/)
- [ChromaDB](https://docs.trychroma.com/)
