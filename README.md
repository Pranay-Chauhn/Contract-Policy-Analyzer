#  Contract and Policy Analyzer

An AI-powered tool built to simplify the way we read and understand complex legal documents — from contracts to privacy policies. This project combines the power of large language models with real-world domain training to make policy analysis smarter, faster, and more reliable.

---

##  Why I Built This

Legal and compliance teams often spend hours parsing through lengthy contracts and dense policies. I wanted to create a solution that saves time, reduces manual errors, and gives quick, accurate insights — without needing a law degree to interpret the fine print.

---

##  What It Does

-  Extracts key clauses, risks, and obligations from contracts  
-  Summarizes long policies into simple language  
-  Flags risky sections or compliance gaps  
-  Provides structured outputs for integration with existing systems  

---

##  Impact & Results

-  Reduced manual review time by **up to 65%** during testing  
-  Accurately extracted legal sections with an **F1 score of 0.84** on a labeled dataset  
-  Summarization BLEU score of **0.71**, delivering high-quality outputs even on lengthy policies  
-  Tested on **150+ real-world documents** (privacy policies, employment contracts, NDAs, etc.)

---

## 🛠 Tech Stack

- **LLM**: Fine-tuned transformer-based models (e.g., Mistral/LLama variants)  
- **NLP**: spaCy, NLTK, custom preprocessing scripts  
- **Frameworks**: HuggingFace Transformers, LangChain  
- **Backend**: Python + FastAPI  
- **Tools**: Git, Docker, (optional Streamlit for UI)

---

##  How I Built It

### 1. **Data Collection & Annotation**
- Gathered real-world contracts, privacy policies, and compliance docs  
- Cleaned and chunked them into meaningful sections  
- Manually labeled clauses, obligations, and risk types for supervised learning

### 2. **Model Fine-Tuning**
- Used a base LLM and fine-tuned it with domain-specific data  
- Applied clause tagging + summarization tasks with customized prompt templates  
- Optimized using F1 and BLEU metrics

### 3. **Inference Pipeline**
- PDF ingestion or raw text → Chunking → Prompt-based inference → Output as structured JSON  
- Risk, clause type, and summary returned via FastAPI

---

##  Example Use Case

Upload an NDA, and the system instantly:
- Extracts all confidentiality clauses
- Flags any automatic renewal risks
- Summarizes key obligations of both parties
- Outputs a clean JSON for legal teams to act on

---

##  Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/contract-policy-analyzer.git
cd contract-policy-analyzer

# Create environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the backend API
python main.py
