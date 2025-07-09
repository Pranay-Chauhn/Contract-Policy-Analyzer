from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
import os
from dotenv import load_dotenv
load_dotenv()


def build_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    memory = ConversationBufferWindowMemory(
        memory_key="chat_history",
        return_messages=True,
        k=5
    )

    llm = ChatOpenAI(
        base_url=os.getenv("LLM_API_BASE_URL"),
        api_key=os.getenv("LLM_API_KEY"),
        model_name=os.getenv("LLM_MODEL_NAME"),
        timeout=360,
        temperature=0.4
    )
    qa_chain = ConversationalRetrievalChain.from_llm(llm=llm,
                                                     memory=memory,
                                                     retriever=retriever,
                                                     return_source_documents=False
                                                     )

    return qa_chain
