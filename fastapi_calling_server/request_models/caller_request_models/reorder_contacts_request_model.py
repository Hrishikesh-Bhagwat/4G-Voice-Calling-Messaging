from pydantic import BaseModel

class ReorderContactsRequestModel(BaseModel):
    new_order: list[str]