from pydantic import BaseModel


class MessageRequest(BaseModel):
    platform: str
    user_id: str
    message: str
