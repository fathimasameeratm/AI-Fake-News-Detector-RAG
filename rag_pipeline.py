from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_classic.chains import RetrievalQA

def create_rag_pipeline(text):

    # Split into chunks
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)

    # Embeddings
    embeddings = HuggingFaceEmbeddings()

    # Vector DB
    vectorstore = FAISS.from_texts(chunks, embeddings)

    # Retriever
    retriever = vectorstore.as_retriever()

    # LLM
    llm = Ollama(model="llama3.2")

    # RAG Chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa