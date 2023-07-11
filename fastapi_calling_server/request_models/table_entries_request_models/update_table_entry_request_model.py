from pydantic import BaseModel

class UpdateTableEntryRequestModel(BaseModel):
    col: str
    id: str
    status: bool