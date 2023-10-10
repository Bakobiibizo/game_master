from typing import Optional, Dict, List
from data_models.message_models import Message, MessageABC, SystemMessageABC, SystemMessage
from helpers.logger import get_logger

logger = get_logger()

class PromptMessage(Message):
    def __init__(self, role, content):
        self.role = role
        self.content = content
        self.create_message()
        
    def create_message(self):
        return self.model_dump()

class PromptMessages(MessageABC):
    def __init__(
        self, 
        role: Optional[str]="user", 
        content: Optional[str]="") -> None:
        self.role = role
        self.content = content
        self.message = Message()

    def create_message(self, role, content)-> Message:
        return self.message.create_message({"role": role, "content": content})



class SystemPromptMessage(SystemMessageABC, SystemMessage):
    def __init__(
        self,
        ) -> None:
        super.__init__()
        self.messages: Optional[List[Message]]=[]
        self.name_map: Optional[Dict[str, str]]={}
        self.message = Message()
                
    def create_system_message(self, content, name):
        role = "system"
        message = self.message.create_message(role, content)
        self.name_map[name] = self.name_map[message]
        self.messages.append(message)
        logger.info("- Created System Message")
        
    def delete_system_message(self, name):
        if name in self.name_map:
            del self.name_map[name]
            logger.info("- Deleted System Message")
        else:
            logger.info("- System Message Not Found")
            
            
        
        
        
        