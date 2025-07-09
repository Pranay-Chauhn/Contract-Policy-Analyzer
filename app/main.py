import streamlit as st
from summary.utils.pdf_utils import extract_text_from_pdf
from summary.chains.summarizer import analyze_policy, analyze_contract
from rag.vectorstore import build_vectorstore_from_text
from rag.ragchain import build_rag_chain

# streamlit design
st.markdown("""
<style>
    /* Background and layout */
    .stApp {
        background-color: #f5f5f5;
    }

    /* Title styling */
    h1 {
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 600;
        margin-bottom: 0.5em;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffffff;
        border-radius: 10px 10px 0 0;
        border: 1px solid #ddd;
        font-weight: bold;
    }

    .stTabs [data-baseweb="tab-panel"] {
        background-color: #ffffff;
        padding: 2rem;
        border: 1px solid #ddd;
        border-top: none;
    }

    /* File uploader and inputs */
    .stFileUploader, .stTextInput {
        background-color: #ffffff;
        padding: 0.5em;
        border-radius: 6px;
        border: 1px solid #ccc;
    }

    /* Buttons */
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 0.6em 1.2em;
        border-radius: 6px;
        border: none;
        font-size: 15px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #45a049;
    }

    /* Subheaders */
    .stMarkdown h2 {
        color: #4CAF50;
        font-size: 1.4rem;
        margin-top: 1.5rem;
    }

    /* Spinner text */
    .stSpinner {
        color: #4CAF50 !important;
    }

</style>
""", unsafe_allow_html=True)

# Configure the page
st.set_page_config(page_title='Contract & Policy Analyzer', layout='wide')
st.title("🧠 Contract & Policy Analyzer")

st.markdown("""
<style>
    .stButton>button {
        border-radius: 8px;
        padding: 0.6em 1em;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📄 Document Settings")

doc_type = st.sidebar.selectbox("Select Document Type", ["Contract", "Policy"])

if doc_type == "Policy":
    policy_type = st.sidebar.selectbox("Select Policy Type", [
        "HR Policy", "Data Protection Policy", "IT Security Policy", "Code of Conduct"
    ])
    contract_type = None
else:
    contract_type = st.sidebar.selectbox("Select Contract Type", [
        "Employment Contract", "Vendor Agreement", "NDA", "Lease Contract"
    ])
    policy_type = None

uploaded_file = st.sidebar.file_uploader("📤 Upload PDF", type=["pdf"])

# Tabs for switching between functionalities
tab1, tab2 = st.tabs(["📑 Summary Analyzer", "💬 Chat with Document"])

if uploaded_file:
    with st.spinner("📚 Extracting content..."):
        text = extract_text_from_pdf(uploaded_file)

    with tab1:
        with st.expander("PDF Preview (Click here...)") :
            st.subheader("📘 PDF Preview")
            st.text_area("Preview", text[:5000], height=300, disabled=True)

        if st.button("📝 Generate Summary"):
            with st.spinner("Analyzing document..."):
                if doc_type == "Policy":
                    result = analyze_policy(text, policy_type)
                else:
                    result = analyze_contract(text, contract_type)

            st.subheader("📊 Summary Result")
            st.write(result)

    with tab2:
        if st.button("🚀 Setup Chatbot"):
            with st.spinner("Embedding & indexing document..."):
                vector_store = build_vectorstore_from_text(text)
                qa_chain = build_rag_chain(vector_store)
                st.session_state.qa_chain = qa_chain
            st.success("✅ Chatbot ready!")

        if "qa_chain" in st.session_state:
            user_question = st.text_input("Ask something about the document:")
            if user_question:
                with st.spinner("Thinking..."):
                    response = st.session_state.qa_chain.run(user_question)
                st.markdown(f"**Answer:** {response}")
else:
    st.info("📂 Please upload a document from the sidebar to get started.")
