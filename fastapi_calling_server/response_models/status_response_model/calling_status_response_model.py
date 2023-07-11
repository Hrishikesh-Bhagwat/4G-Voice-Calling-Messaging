from pydantic import BaseModel

class CallingStatusResponseModel(BaseModel):
    id: str
    type: str
    message: str