import uuid
from utils.database_utils.db_ops import load_db, save_db

def get_contacts():
    db=load_db()
    return db["callers"]

def add_contact(name,phone):
    random_uuid = uuid.uuid4()
    random_uuid_str = str(random_uuid)
    db=load_db()
    db["callers"].append(
        {
            "name":name,
            "phone":phone,
            "id":random_uuid_str,
            "selected": False
        }
    )
    save_db(db)

def delete_contact(id):
    db=load_db()
    contacts=db["callers"]
    final_list=[]
    for i in contacts:
        if i["id"]!=id:
            final_list.append(i)
    db["callers"]=final_list
    save_db(db)

def set_contact_status(id,value):
    db=load_db()
    contacts=db["callers"]
    for i in range(len(contacts)):
        if contacts[i]["id"]==id:
            contacts[i]["selected"]=value
    db["callers"]=contacts
    save_db(db)

