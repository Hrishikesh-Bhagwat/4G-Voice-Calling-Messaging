from pydantic import BaseModel

class AddContactRequestModel(BaseModel):
    name: str
    phone: str