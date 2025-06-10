import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI client
client = OpenAI(api_key="bro thought ill put my api key smh ##put your api key")

# Streamlit settings
st.set_page_config(page_title="File Search Assistant", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for dark mode
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput>div>div>input {
        color: white;
        background-color: #262730;
    }
    .stButton>button {
        background-color: #40444b;
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🔍 File Search Assistant")
st.markdown("Use natural language to search through your uploaded files.")

# User input
user_input = st.text_input("Ask something about your files", placeholder="e.g., search client address and put it into csv format")

# Submit button
if st.button("Send") and user_input:
    with st.spinner("Searching..."):
        input_messages = [{"role": "user", "content": user_input}]

        tools = [
            {
                "type": "file_search",
                "vector_store_ids": [os.getenv("VECTOR_STORE_ID", "smh(again) ##  put your vector store id")],
                "max_num_results": 3
            }
        ]

        try:
            response = client.responses.create(
                model="gpt-4o-mini",
                instructions="You are a helpful assistant.",
                input=input_messages,
                tools=tools,
                include=["file_search_call.results"]
            )

            # Output message
            for output_item in response.output:
                if output_item.type == "file_search_call":
                    st.subheader("📁 Search Results")
                    for i, result in enumerate(output_item.results, 1):
                        st.markdown(f"*Result {i}*")
                        st.text(f"Filename: {result.filename}")
                        st.text(f"Score: {result.score:.2f}")
                        st.code(result.text[:300] + "..." if len(result.text) > 300 else result.text)

                if output_item.type == "message":
                    st.subheader("🧠 Assistant Response")
                    for content_item in output_item.content:
                        if content_item.type == "output_text":
                            st.markdown(content_item.text)

                            if hasattr(content_item, "annotations"):
                                st.subheader("📚 Citations")
                                for annotation in content_item.annotations:
                                    if annotation.type == "file_citation":
                                        st.markdown(f"- Cited from file: {annotation.filename}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
