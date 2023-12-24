import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
import openai

def pdf_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:  # Check if text is extracted
                text += page_text
    return text

def get_text_chucks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chucks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(text_chucks, embeddings)
    return vector_store

def simple_text_summary(text, max_length=500):
    """ Generate a simple summary by truncating the text. """
    return text[:max_length]

def main():
    load_dotenv()
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    
    st.set_page_config(page_title="Chatting with multi-PDF doc-bot", page_icon='📄')
    st.header("Chatting with multi-PDF doc-bot")

    # Chat input
    user_input = st.text_input("Ask questions about your documents:")
    
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDF documents here and click on 'Processing'", accept_multiple_files=True)

        if st.button("Processing") and pdf_docs:
            with st.spinner("Processing your documents..."):
                # Extract PDF text
                raw_text = pdf_pdf_text(pdf_docs)
                
                # Generate text summary
                summary = simple_text_summary(raw_text)

                # Display the summary
                st.subheader("Document Summary")
                st.write(summary)

                # Get chunks of text
                text_chucks = get_text_chucks(raw_text)
                
                # Create vector store (or any other processing you need)
                vector_store = get_vectorstore(text_chucks)

            # You can process the user input here, as needed

if __name__ == '__main__':
    main()
