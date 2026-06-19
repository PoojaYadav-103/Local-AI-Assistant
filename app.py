import os
from dotenv import load_dotenv

load_dotenv()

print("PROJECT:", os.getenv("LANGCHAIN_PROJECT"))
print("TRACING:", os.getenv("LANGCHAIN_TRACING_V2"))

os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Streamlit Page Configuration

st.set_page_config(
    page_title="Local AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main-title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#4F8BF9;
    margin-bottom:5px;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:25px;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)



# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a friendly and helpful AI assistant. "
            "Give clean, structured and easy to understand answers."
        ),
        (
            "user",
            "{question}"
        )
    ]
)

# LLM

llm = ChatOllama(

    model="llama3.2",
    temperature=0

)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# Session State

if "messages" not in st.session_state:

    st.session_state.messages = []

# Header

st.markdown(

    '<div class="main-title">🤖 Local AI Assistant</div>',

    unsafe_allow_html=True

)

st.markdown(

    '<div class="subtitle">Powered by LangChain + Ollama + Llama 3.2</div>',

    unsafe_allow_html=True

)

# Display Previous Messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# Chat Input

user_input = st.chat_input("Ask me anything...")

if user_input:

    st.session_state.messages.append(

        {

            "role": "user",

            "content": user_input

        }

    )

    with st.chat_message("user"):

        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = chain.invoke(

                {

                    "question": user_input

                }

            )

        st.markdown(response)

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": response

        }

    )

# Footer


st.markdown("---")

st.caption(
    "Built with Streamlit • LangChain • Ollama • Llama3.2"
)
