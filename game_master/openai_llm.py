import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from helpers.logger import get_logger

logger = get_logger()

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def openai_llm_chain(memory, prompt):
    logger.info("- Loading OpenAI")
    
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)    

    logger.info("- Running LLM")

    chain = llm.create_chain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        )

    return chain


