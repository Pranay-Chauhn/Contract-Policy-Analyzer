from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.chains import LLMChain
from openai import base_url
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
    prompt = PromptTemplate.from_template(get_policy_prompt(policy_type))
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(context=text[:3000])


def analyze_contract(text):
    prompt = PromptTemplate.from_template(get_contract_prompt())
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(context=text[:3000])
