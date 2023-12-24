import streamlit as st 
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def pdf_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:  # Check if text is extracted
                text += page_text
    return text

def get_text_chucks(raw_text):

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
                st.write(raw_text)
                #get chuck of text
                text_chucks = get_text_chucks(raw_text)
#               #create vector store

if __name__ == '__main__':
    main()
