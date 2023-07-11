from pydantic import BaseModel

class GetContactsResponseModel(BaseModel):
    name: str
    phone: str
    id: str
    selected: bool