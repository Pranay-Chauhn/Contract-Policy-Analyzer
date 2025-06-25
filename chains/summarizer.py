from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.chains import LLMChain
from openai import base_url
from utils.prompt import get_contract_prompt, get_policy_prompt

llm = ChatOpenAI(
    base_url="http://192.168.1.34:1234/v1",
    api_key="lmstudio",
    model_name="meta-llama-3.1-8b-instruct"
)


def analyze_policy(text, policy_type):
    prompt = PromptTemplate.from_template(get_policy_prompt(policy_type))
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(context=text[:3000])


def analyze_contract(text):
    prompt = PromptTemplate.from_template(get_contract_prompt())
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(context=text[:3000])
