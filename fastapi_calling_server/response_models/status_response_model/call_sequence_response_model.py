from pydantic import BaseModel

class CallSequenceResponseModel(BaseModel):
    is_free: bool