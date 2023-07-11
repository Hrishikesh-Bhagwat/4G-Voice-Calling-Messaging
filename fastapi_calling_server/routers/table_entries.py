from fastapi import APIRouter, File, UploadFile, Form
from response_models.table_response_models.get_table_error_response_model import GetTableErrorResponseModel
from response_models.table_response_models.get_table_response_model import TableResponseModel
from response_models.table_response_models.add_entry_response_model import AddTableEntryResponseModel
from response_models.table_response_models.delete_table_entry_response_model import DeleteTableEntryResponseModel
from response_models.table_response_models.update_heading_response_model import UpdateHeadingResponseModel
from response_models.table_response_models.update_table_entry_response_model import UpdateTableEntryResponseModel

import uuid
import os
import shutil
from utils.database_utils.table_ops import get_table_entries, add_to_table, delete_table_entry, update_heading, update_selection
from utils.database_utils.db_path import main_path
from utils.database_utils.db_path import ser_path
from request_models.table_entries_request_models.delete_table_entry_request_model import DeleteTableEntryRequestModel
from request_models.table_entries_request_models.update_table_entry_request_model import UpdateTableEntryRequestModel
from serial import Serial
router = APIRouter()

is_gsm_ok=False

@router.get("/",response_model=TableResponseModel)
def get_table():
    return get_table_entries()

@router.post("/add-entry",response_model=AddTableEntryResponseModel)
async def add_entry_to_table(file: UploadFile = File(...), text: str = Form(...), col: str=Form(...)):
    random_uuid = uuid.uuid4()
    random_uuid_str = str(random_uuid)
    file_path=os.path.join(main_path,col,random_uuid_str+".mp3")
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    add_to_table(col,text,file_path,random_uuid_str)
    return {"status":file.filename}

@router.post("/delete-entry",response_model=DeleteTableEntryResponseModel)
async def delete_table_entry_handler(delete_table_entry_request_model: DeleteTableEntryRequestModel):
    col=delete_table_entry_request_model.column_id
    entry_id=delete_table_entry_request_model.entry_id
    delete_table_entry(col,entry_id)
    return {"status":True}

@router.post("/update-heading",response_model=UpdateHeadingResponseModel)
async def update_heading_request_handler(file: UploadFile = File(...), text: str = Form(...), col: str=Form(...)):
    # random_uuid = uuid.uuid4()
    # random_uuid_str = str(random_uuid)
    file_path=os.path.join(main_path,"headings",col+".mp3")
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    update_heading(col,text,file_path)
    return {"status":True}

@router.post("/update-state",response_model=UpdateTableEntryResponseModel)
async def update_table_entry_status(update_table_entry_request_model: UpdateTableEntryRequestModel):
    update_selection(update_table_entry_request_model.col,update_table_entry_request_model.id,update_table_entry_request_model.status)
    return {"status":True}
    

    