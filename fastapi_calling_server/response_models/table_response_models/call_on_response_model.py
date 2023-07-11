from pydantic import BaseModel

class CallOnResponseModel(BaseModel):
    is_on: bool