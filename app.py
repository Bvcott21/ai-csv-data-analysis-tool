import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

load_dotenv()

st.title("Let's do some analysis on your csv.")
st.header("Please upload your csv file here:")

# Capture the csv file
data = st.file_uploader("Upload csv file", type="csv")

query = st.text_area("Enter your query")
button = st.button("Generate response")

if button:
    #Get response
    answer = query_agent(data, query)
    st.write(answer)