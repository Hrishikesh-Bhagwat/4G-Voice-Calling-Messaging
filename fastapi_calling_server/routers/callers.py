from fastapi import APIRouter
from utils.database_utils import contact
from typing import List
from response_models.caller_response_models.get_contacts_response_model import GetContactsResponseModel
from response_models.caller_response_models.delete_contact_response_model import DeleteContactsResponseModel
from response_models.caller_response_models.add_contact_response_model import AddContactResponseModel
from response_models.caller_response_models.update_contact_response_model import UpdateContactResponseModel

from request_models.caller_request_models.delete_contact_request_model import DeleteContactRequestModel
from request_models.caller_request_models.add_contact_request_model import AddContactRequestModel
from request_models.caller_request_models.update_contact_status_request_model import UpdateContactRequestModel
from utils.database_utils.contact import delete_contact, add_contact, set_contact_status

router = APIRouter()

@router.get("/",response_model=List[GetContactsResponseModel])
async def read_contacts():
    contacts = contact.get_contacts()
    return contacts

@router.post("/delete-contact",response_model=DeleteContactsResponseModel)
async def delete_contact_handler(delete_contact_request_model: DeleteContactRequestModel):
    delete_contact(delete_contact_request_model.id)
    return {"status":True}

@router.post("/add-contact",response_model=AddContactResponseModel)
async def create_new_contact(add_contact_request_model: AddContactRequestModel):
    add_contact(add_contact_request_model.name,add_contact_request_model.phone)
    return {"status":True}

@router.post("/update-status",response_model=UpdateContactResponseModel)
async def update_contact_status(update_contact_request_model: UpdateContactRequestModel):
    set_contact_status(update_contact_request_model.id,update_contact_request_model.status)
    return {"status":True}
    
    
