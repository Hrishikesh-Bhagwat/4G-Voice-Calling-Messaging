from pydantic import BaseModel

class DeleteContactRequestModel(BaseModel):
    id: str