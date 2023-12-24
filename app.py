import streamlit as st 
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="Chatting with multi-PDF doc-bot", page_icon='📄')
    st.header("Chatting with multi-PDF doc-bot")
    st.text_input("Ask questions about your documents:")
    
    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload your PDF documents here and click on 'Processing' ")
        st.button("Processing")

if __name__ == '__main__':
    main()

