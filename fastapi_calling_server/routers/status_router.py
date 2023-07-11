from fastapi import APIRouter
from response_models.status_response_model.status_response_model import StatusResponseModel
from response_models.table_response_models.call_on_response_model import CallOnResponseModel
from utils.gsm_utils import GSMStatus

router = APIRouter()
@router.get("/",response_model=StatusResponseModel)
def get_status():
    return {"message":GSMStatus.message,"error":GSMStatus.is_error}