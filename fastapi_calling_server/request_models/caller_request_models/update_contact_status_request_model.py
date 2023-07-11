from pydantic import BaseModel

class UpdateContactRequestModel(BaseModel):
    id: str
    status: bool