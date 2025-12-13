import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Load Documents
print("Loading documents...")
loader = DirectoryLoader(
    '../book/book/ai-interactive-textbook/docs',
    glob="**/*.md*",
    loader_cls=TextLoader,
    show_progress=True,
    use_multithreading=True
)
documents = loader.load()
print(f"Loaded {len(documents)} documents.")

# 2. Split Text
print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)
print(f"Split into {len(chunks)} chunks.")

# 3. Create Embeddings
print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Create and Save FAISS Vector Store
print("Creating and saving FAISS vector store...")
vector_store = FAISS.from_documents(chunks, embeddings)
vector_store.save_local("faiss_index")

print("Knowledge base created successfully.")
