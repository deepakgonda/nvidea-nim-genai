import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA

# Load environment variables
load_dotenv()
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

# ✅ Initialize NVIDIA Embeddings
nvidia_embeddings = NVIDIAEmbeddings(
    model="nvidia/llama-3.2-nv-embedqa-1b-v2",
    api_key=NVIDIA_API_KEY,
    truncate="NONE"
)

# ✅ Initialize NVIDIA Chat Model
chat_client = ChatNVIDIA(
    model="meta/llama-3.3-70b-instruct",
    api_key=NVIDIA_API_KEY,
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024
)

# ✅ Initialize ChromaDB with NVIDIA Embeddings
vector_store = Chroma(
    persist_directory=None,  # In-memory for now
    embedding_function=nvidia_embeddings
)

# ✅ Load and store vectors with force rebuild
def load_text_and_store_vectors(filename="data.txt", force_rebuild=False):
    if force_rebuild and os.path.exists("./chroma_db"):
        import shutil
        shutil.rmtree("./chroma_db")
        print("🗑️ Existing ChromaDB cleared!")

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_text(text)

    # Store text in ChromaDB (embeddings auto-generated)
    vector_store.add_texts(texts)
    print("✅ Knowledge stored in vector database!")

# ✅ Retrieve Context Function with Logging
def retrieve_relevant_context(query):
    docs = vector_store.similarity_search(query, k=3)
    print(f"🔍 Retrieved {len(docs)} relevant documents from ChromaDB:")
    for idx, doc in enumerate(docs, start=1):
        print(f"📄 Document {idx}: {doc.page_content}\n")

    return "\n".join([doc.page_content for doc in docs])

# ✅ Chat Function using NVIDIA's Chat Model with Streaming and Logging
def chat_with_ai():
    print("💬 RAG Chatbot (Type 'exit' to stop)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        # Retrieve relevant context from ChromaDB
        context = retrieve_relevant_context(user_input)

        # Construct the final prompt
        prompt = f"Context:\n{context}\n\nUser Question: {user_input}"
        print(f"📝 Final Prompt Sent to NVIDIA:\n{prompt}\n")

        # Stream response from NVIDIA chat model
        print("🤖 NVIDIA AI Response: ", end="")
        for chunk in chat_client.stream([{"role": "user", "content": prompt}]):
            print(chunk.content, end="")
        print("\n")  # For proper formatting

# ✅ Main Execution
if __name__ == "__main__":
    # Force rebuild database on every run
    load_text_and_store_vectors(force_rebuild=True)
    chat_with_ai()
