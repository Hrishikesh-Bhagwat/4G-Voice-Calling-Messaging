from pydantic import BaseModel

class DeleteContactsResponseModel(BaseModel):
    status: bool