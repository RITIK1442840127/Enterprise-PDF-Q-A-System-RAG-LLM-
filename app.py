import streamlit as st
from rag_pipeline import load_and_split, create_vector_store, get_answer

st.title("📄 PDF Q&A System (RAG)")

pdf = st.file_uploader("Upload PDF", type="pdf")

if pdf:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    docs = load_and_split("temp.pdf")
    db = create_vector_store(docs)

    query = st.text_input("Ask your question:")

    if query:
        answer = get_answer(query, db)
        st.write("### Answer:")
        st.write(answer)