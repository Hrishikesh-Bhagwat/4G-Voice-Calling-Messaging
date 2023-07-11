from utils.database_utils.contact import get_contacts
from utils.database_utils.table_ops import get_table_entries
from utils.gsm_utils import CallingStatus
import uuid
from utils.database_utils.db_path import gsm_server
import requests
import json
import time
import os
# from pygame import mixer

# def play_clip(path):
#     if os.path.exists(path):
#         mixer.init()
#         mixer.music.load(path)
#         mixer.music.play()
#         while mixer.music.get_busy():
#             continue


def get_selected_contacts():
    contacts=get_contacts()
    temp=[]
    for i in contacts:
        if i["selected"]==True:
            temp.append(i)
    return temp

def get_selected_options():
    table=get_table_entries()
    pairs=[]
    for i in table["col1"]["entries"]:
        if i["selected"]==True:
            pairs.append({
                "heading":table["col1"]["heading"],
                "entry":i
            })
    for i in table["col2"]["entries"]:
        if i["selected"]==True:
            pairs.append({
                "heading":table["col2"]["heading"],
                "entry":i
            })
    for i in table["col3"]["entries"]:
        if i["selected"]==True:
            pairs.append({
                "heading":table["col3"]["heading"],
                "entry":i
            })
    for i in table["col4"]["entries"]:
        if i["selected"]==True:
            pairs.append({
                "heading":table["col4"]["heading"],
                "entry":i
            })
    for i in table["col5"]["entries"]:
        if i["selected"]==True:
            pairs.append({
                "heading":table["col5"]["heading"],
                "entry":i
            })
    for i in table["col6"]["entries"]:
        if i["selected"]==True:
            pairs.append({
                "heading":table["col6"]["heading"],
                "entry":i
            })
    return pairs

def split_sentence(sentence, max_length=130):
    words = sentence.split()
    result = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_length:
            if current_line:
                current_line += " "
            current_line += word
        else:
            result.append(current_line)
            current_line = word

    if current_line:
        result.append(current_line)

    return result

def update_calling_status(message,type):
    random_uuid = uuid.uuid4()
    random_uuid_str = str(random_uuid)
    CallingStatus.id=random_uuid_str
    CallingStatus.message=message
    CallingStatus.type=type


def emergency_process():
    # set is_busy to true
    CallingStatus.is_call_active=True
    # set alert options in class
    update_calling_status("Starting emergency procedure","info")
    contacts=get_selected_contacts()
    pairs=get_selected_options()
    res=requests.get(gsm_server+"/diagnostics")
    if res.status_code!=200:
        update_calling_status(f"Diagnostics failed ","error")
        time.sleep(2.5)
        CallingStatus.is_call_active=False
        return
    if json.loads(res.text)["is_error"]==True:
        if "Weak network" in json.loads(res.text)["message"]:
            update_calling_status("Continuing with weak network","warning")
            time.sleep(2.5)            
        else:
            update_calling_status(f"Diagnostics failed","error")
            time.sleep(2.5)
            CallingStatus.is_call_active=False
            return
    # message=[]
    # c=''
    # for i in pairs:
    #     if len(c+" "+i["heading"]["title"]+" "+i["entry"]["text"])<130:
    #         c=c+" "+i["heading"]["title"]+" "+i["entry"]["text"]
    #     else:
    #         message.append(c)
    #         c=i["heading"]["title"]+" "+i["entry"]["text"]

    if len(pairs)!=0 and len(contacts)!=0:
        new_pairs=[]
        for i in pairs:
            new_pairs.append({"heading":i["heading"]["file"],"entry":i["entry"]["file"]})
        for i in contacts:
            update_calling_status(f"Calling {i['name']}({i['phone']})","info")
            is_failed=False
            res=requests.post(gsm_server+"/make-call",json={'pairs':new_pairs,'phone':i["phone"]})
            if res.status_code!=200:
                update_calling_status(f"Calling {i['name']}({i['phone']}) failed","error")
                time.sleep(2.5)

            response_body=json.loads(res.text)
            if response_body['status']==False:
                print(response_body["message"])
                update_calling_status(response_body["message"],"error")
                time.sleep(2.5)
            
            else:
                update_calling_status(f"Calling {i['name']}({i['phone']}) successful!","success")
                time.sleep(2.5)


        sentence=pairs[0]["heading"]["title"]+" "+pairs[0]["entry"]["text"]
        for i in range(1,len(pairs)):
            sentence+=(pairs[i]["heading"]["title"]+" "+pairs[i]["entry"]["text"])
        message=split_sentence(sentence,130)
        for i in contacts:
            update_calling_status(f"Messaging {i['name']}({i['phone']})","info")
            is_failed=False
            for j in message:
                res=requests.post(gsm_server+"/send-sms",json={'text':j,'phone':i['phone']})
                if res.status_code!=200:
                    print("Status:",res.status_code)
                    update_calling_status(f"Sending sms to {i['name']}({i['phone']}) failed","error")
                    is_failed=True
                    break
                response_body=json.loads(res.text)
                if response_body['status']==False:
                    print(response_body["message"])
                    update_calling_status(response_body["message"],"error")
                    is_failed=True
                    break
            if is_failed:
                time.sleep(2.5)
            if not is_failed:
                print("All ok!")
                update_calling_status(f"Sent sms to {i['name']}({i['phone']})","success")
                time.sleep(3)

    update_calling_status("Emergency Sequence complete","success")
    CallingStatus.is_call_active=False