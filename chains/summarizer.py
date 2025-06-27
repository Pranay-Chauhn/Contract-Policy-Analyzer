from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.chains import LLMChain
from openai import base_url

from utils.chunks import split_to_chunks
from utils.prompt import get_contract_prompt, get_policy_prompt
from dotenv import load_dotenv
import os

# load env
load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("LLM_API_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    model_name=os.getenv("LLM_MODEL_NAME")
)


def analyze_policy(text, policy_type):
    prompt_template = get_policy_prompt(policy_type)
    prompt = PromptTemplate.from_template(prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)

    chunks = split_to_chunks(text)
    summaries = []

    for i, chunk in enumerate(chunks):
        summary = chain.run(context=chunk.page_content)
        summaries.append(f"### Section {i + 1}\n {summary}")

    combined_summaries = "\n\n".join(summaries)
    final_prompt_template = f"""
You are an assistant summarizing a summarized corporate {policy_type}.
Summarize the key points in the following areas:
- Purpose of the policy in short summary  
- Rules mentioned (leave, work hours, conduct, etc.). Where possible, include specific numbers, durations, or thresholds mentioned in the policy (e.g., “12 casual leaves/year”, “shift time 9–6”).
- Any compliance/legal mentions
- Summary in plain English

Text:
{{context}}
"""
    final_prompt = PromptTemplate.from_template(final_prompt_template)
    final_chain = LLMChain(llm=llm, prompt=final_prompt)
    final_summary = final_chain.run(context=combined_summaries)

    return final_summary


def analyze_contract(text):
    prompt_template = get_contract_prompt()
    prompt = PromptTemplate.from_template(prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)

    chunks = split_to_chunks(text)
    summaries = []

    for i, chunk in enumerate(chunks):
        summary = chain.run(context=chunk.page_content)
        summaries.append(f"### Section {i + 1}\n {summary}")

    return "\n\n".join(summaries)


def combine_summaries(summaries):
    final_prompt = PromptTemplate.from_template("""
You are an Corporate. Summarize the following chunked summaries into one cohesive HR policy overview.

Summaries:
{context}
""")
    combine_chain = LLMChain(llm=llm, prompt=final_prompt)
    return combine_chain.run(context=summaries)
