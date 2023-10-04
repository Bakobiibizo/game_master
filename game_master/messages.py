from typing import Optional, Dict, List
from data_models.message_models import Message, MessageABC, SystemMessageABC, SystemMessage
from helpers.logger import get_logger

logger = get_logger()


class PromptMessages(MessageABC):
    def __init__(
        self, 
        role: Optional[str]="user", 
        content: Optional[str]="") -> None:
        super.__init__(self)
        self.role = role
        self.content = content

    def create_message(self, role, content)-> Dict[str, str]:
        return {"role": role, "content": content}


class SystemPromptMessage(SystemMessageABC):
    def __init__(
        self,
        ) -> None:
        super.__init__(SystemMessage)
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
            
            
        
        
        
        