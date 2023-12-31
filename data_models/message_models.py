"""
A module for message creation and management. Everyone seem to have adopted the OpenAI messaging format so I decided to follow suit. 
message = [{
    "role": "user/assistant/system",
    "content":"some content"
}]
Everything I will add will be in this format.
"""
from typing import List, Dict, Union
from abc import ABC, abstractmethod
from enum import Enum
from pydantic import BaseModel

class Message(BaseModel):
    """
    Pydantic model for data sent and recieved by the agent
    """
    role: str
    content: str

class SystemMessage(BaseModel):
    """
    Model for managing system messages
    """
    messages: List[Message]
    name_map: Dict[str, str]

def message_sql_table():
    return """
    CREATE TABLE IF NOT EXISTS agent_actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (message_id) REFERENCES message (id)
);"""

class MessageABC(ABC):
    """
    Abstract base class for message models
    """
    @abstractmethod
    def create_message(self, role:str, content: str)-> Dict[str, str]:
        """
        Convert role and content into message object
        """

class SystemMessageABC(ABC):
    """"
    Abstract base class for System Messages
    """
    @abstractmethod
    def create_system_message(self, content: str, name: str) -> None:
        """
        Convert role and content into message dict
        """
    @abstractmethod
    def delete_system_message(self)-> None:
        """
        Delete a system message from the system messages
        """
    @abstractmethod
    def edit_system_message(self)-> None:
        """
        Edit a system message in system messages
        """
