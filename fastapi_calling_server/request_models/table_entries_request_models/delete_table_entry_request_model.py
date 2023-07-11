from pydantic import BaseModel

class DeleteTableEntryRequestModel(BaseModel):
    column_id: str
    entry_id: str