# load libraries and dependencies

import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredDocumentLoader
import os

# env
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]

llm = ChatOpenAI(temperature=0, max_tokens=1000, model_name="gpt-3.5-turbo")

# chatbot title
st.title = "Chat with LangChain"

# File uploader in sidebar