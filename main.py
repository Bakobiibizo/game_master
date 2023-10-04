from helpers.logger import get_logger
from game_master.openai_llm import openai_llm_chain
from data_models.message_models import Message
from game_master.datastax_vectordb import get_memory_module, connection_to_cluster

logger = get_logger()

messages = Message


def main():
    prompt = input("Enter your prompt: ")
    role = "user"
    session =  connection_to_cluster()
    memory = get_memory_module(session)
    message = messages(role=role, content=prompt).model_dump()
    response = openai_llm_chain(prompt=message, memory=memory)
    logger.debug(response)    


    


if __name__ == "__main__":
    main()