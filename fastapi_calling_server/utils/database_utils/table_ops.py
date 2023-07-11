from utils.database_utils.db_ops import load_db, save_db

def get_table_entries():
    db=load_db()
    col1=db["col1"]
    col2=db["col2"]
    col3=db["col3"]
    col4=db["col4"]
    col5=db["col5"]
    col6=db["col6"]
    text=""
    for i in col1["items"]:
        if i["selected"]:
            text+=(col1["title"]+" "+i["text"]+". ")
    for i in col2["items"]:
        if i["selected"]:
            text+=(col2["title"]+" "+i["text"])
    for i in col3["items"]:
        if i["selected"]:
            text+=(col3["title"]+" "+i["text"])
    for i in col4["items"]:
        if i["selected"]:
            text+=(col4["title"]+" "+i["text"])
    for i in col5["items"]:
        if i["selected"]:
            text+=(col5["title"]+" "+i["text"])
    for i in col6["items"]:
        if i["selected"]:
            text+=(col6["title"]+" "+i["text"])
    return {
        "text":text,
        "status": True,
        "col1":{
            "heading":{
                "title":col1["title"],
                "file":col1["path"]
            },
            "entries":col1["items"]
        },
        "col2":{
            "heading":{
                "title":col2["title"],
                "file":col2["path"]
            },
            "entries":col2["items"]
        },
        "col3":{
            "heading":{
                "title":col3["title"],
                "file":col3["path"]
            },
            "entries":col3["items"]
        },
        "col4":{
            "heading":{
                "title":col4["title"],
                "file":col4["path"]
            },
            "entries":col4["items"]
        },
        "col5":{
            "heading":{
                "title":col5["title"],
                "file":col5["path"]
            },
            "entries":col5["items"]
        },
        "col6":{
            "heading":{
                "title":col6["title"],
                "file":col6["path"]
            },
            "entries":col6["items"]
        }
    }

def add_to_table(col,text,path,id):
    db=load_db()
    entries=db[col]["items"]
    # random_uuid = uuid.uuid4()
    # random_uuid_str = str(random_uuid)
    entries.append(
        {
            "text": text,
            "file": path,
            "id": id,
            "selected": False
        }
    )
    db[col]["items"]=entries
    save_db(db)

def update_heading(col,title,path):
    db=load_db()
    db[col]["title"]=title
    db[col]["path"]=path
    save_db(db)

def update_selection(col,id,value):
    db=load_db()
    entries=db[col]["items"]
    for i in range(len(entries)):
        entries[i]["selected"]=False
    for i in range(len(entries)):
        if entries[i]["id"]==id:
            entries[i]["selected"]=value
    db[col]["items"]=entries
    save_db(db)

def delete_table_entry(col,id):
    db=load_db()
    entries=db[col]["items"]
    final_entries=[]
    for i in entries:
        if i["id"]!=id:
            final_entries.append(i)
    db[col]["items"]=final_entries
    save_db(db)

def update_table_heading(col,title,path):
    db=load_db()
    db[col]["title"]=title
    db[col]["path"]=path
    save_db(db)
