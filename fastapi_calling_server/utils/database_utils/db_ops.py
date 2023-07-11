from utils.database_utils.db_path import database_path
import json

def load_db():
    with open(database_path,"r") as f:
        return json.load(f)

def save_db(write_dict):
    with open(database_path,"w") as f:
        json.dump(write_dict,f,indent=6)
    return True