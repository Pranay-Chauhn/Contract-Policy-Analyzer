import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from chains.summarizer import analyze_policy, analyze_contract


st.set_page_config(page_title='Contract &  Policy Analyzer', layout='wide')

st.title("Contract / Policy Analyzer")

# Sidebar Options
st.sidebar.header("Document Settings")
doc_type = st.sidebar.selectbox("Select Document Type", ["Contract", "Policy"])

policy_type = None
if doc_type == "Policy":
    policy_type = st.selectbox("Select the Policy type",[
        "HR Policy", "Data Protection Policy", "IT Security Policy", "Code of Conduct"
                               ])
uploaded_file = st.file_uploader("Upload a PDF Document", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting content from file..."):
        text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Text ...")
    st.code(text[:1000])

    if st.button("Analyze"):
        with st.spinner("Analyzing document"):
            if doc_type == "Policy" :
                result = analyze_policy(text, policy_type)
            else :
                result = analyze_contract(text)

        st.subheader("Analysis Result")
        st.write(result)


