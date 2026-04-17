from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ✅ Load model once (fast)
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


# ✅ Step 1: Load & Split PDF
def load_and_split(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Clean text
    for doc in documents:
        doc.page_content = doc.page_content.replace("\n", " ").strip()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    return splitter.split_documents(documents)


# ✅ Step 2: Create Vector DB
def create_vector_store(docs):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    db = FAISS.from_documents(docs, embeddings)
    return db


# ✅ Step 3: Get Answer (FINAL)
def get_answer(query, db):
    retriever = db.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)

    if not docs:
        return "I don't know"

    context = "\n".join([doc.page_content for doc in docs])

    # Basic safety check
    if len(context.strip()) < 50:
        return "I don't know"

    prompt = f"""
    Answer the question using ONLY the context below.

    If the answer is not clearly mentioned, say:
    "I don't know"

    Do not guess. Be precise.

    Context:
    {context}

    Question:
    {query}
    """

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_length=200
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer