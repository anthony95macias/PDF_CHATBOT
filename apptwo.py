# import streamlit as st 
# from dotenv import load_dotenv
# from PyPDF2 import PdfReader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings, SentenceTransformerEmbeddings
# from langchain.vectorstores import FAISS

# def pdf_pdf_text(pdf_docs):
#     text = ""
#     for pdf in pdf_docs:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             page_text = page.extract_text()
#             if page_text:  # Check if text is extracted
#                 text += page_text
#     return text

# def get_text_chucks(text):
#     text_splitter = CharacterTextSplitter(
#         separator="\n",
#         chunk_size=1000,
#         chunk_overlap=200,
#         length_function=len
#     )
#     chunks = text_splitter.split_text(text)
#     return chunks

# def get_vectorstore(text_chucks):
#     embeddings = HuggingFaceEmbeddings(model_name="hkunlp/instructor-xl")
#     vector_store = FAISS.from_texts(text_chucks, embeddings)
#     return vector_store
    

# def main():
#     load_dotenv()
#     st.set_page_config(page_title="Chatting with multi-PDF doc-bot", page_icon='📄')
#     st.header("Chatting with multi-PDF doc-bot")
#     st.text_input("Ask questions about your documents:")
    
#     with st.sidebar:
#         st.subheader("Your Documents")
#         pdf_docs = st.file_uploader("Upload your PDF documents here and click on 'Processing'", accept_multiple_files=True)
#         if st.button("Processing") and pdf_docs:
#             with st.spinner("Processing your documents..."):
                
#                 #pdf raw text
#                 raw_text = pdf_pdf_text(pdf_docs)
                
#                 #get chuck of text
#                 text_chucks = get_text_chucks(raw_text)
                
#                 #create vector store
#                 vector_store = get_vectorstore(text_chucks)

# if __name__ == '__main__':
#     main()



import streamlit as st 
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def pdf_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
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
    try:
        # Using default settings for HuggingFaceEmbeddings
        embeddings = HuggingFaceEmbeddings()
        vector_store = FAISS.from_texts(text_chucks, embeddings)
        return vector_store
    except Exception as e:
        st.error(f"Failed to create vector store: {e}")
        return None

def main():
    load_dotenv()
    st.set_page_config(page_title="Chatting with multi-PDF doc-bot", page_icon='📄')
    st.header("Chatting with multi-PDF doc-bot")
    st.text_input("Ask questions about your documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDF documents here and click on 'Processing'", accept_multiple_files=True)
        if st.button("Processing") and pdf_docs:
            with st.spinner("Processing your documents..."):
                raw_text = pdf_pdf_text(pdf_docs)
                text_chucks = get_text_chucks(raw_text)
                vector_store = get_vectorstore(text_chucks)
                if vector_store is not None:
                    st.success("Documents processed successfully.")

if __name__ == '__main__':
    main()
