from pydantic import BaseModel

class StatusResponseModel(BaseModel):
    message: str
    error: bool