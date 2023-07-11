from fastapi import FastAPI
from response_models.status_response_model.status_response_model import StatusResponseModel
from response_models.status_response_model.calling_status_response_model import CallingStatusResponseModel
from routers.callers import router as contacts_router
from routers.table_entries import router as table_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from utils.database_utils.db_path import gsm_server
from fastapi.responses import RedirectResponse
import requests
import json
import uvicorn
from fastapi import BackgroundTasks
from fastapi.staticfiles import StaticFiles
from utils.gsm_utils import GSMStatus, CallingStatus
from utils.emergency_utils import emergency_process
from response_models.status_response_model.call_sequence_response_model import CallSequenceResponseModel

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:3001",
    "http://localhost:3002/",
    "*"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

res={
    "message":"",
    "is_error":False
}
phone={
    "is_active":True,
    "message":"Calling Mihir (9820238399)"
}
# @app.on_event("startup")
# @repeat_every(seconds=60*3)
# def add_diagnostic_task()->None:
#     res=requests.get(gsm_server+"/diagnostics")
#     data=json.loads(res.content)
#     GSMStatus.message=data["message"]
#     GSMStatus.is_error=data["is_error"]

app.mount("/static", StaticFiles(directory="/root/Nagarjuna/fastapi_calling_server/static",html=True), name="static")

app.include_router(contacts_router,prefix="/contacts",tags=["Contacts API"])
app.include_router(table_router,prefix="/table-entries",tags=["Table Entries"])
# app.include_router(call_sequence_router,prefix="/call-sequence",tags=["Call Sequence"])

@app.get("/calling-status",response_model=CallingStatusResponseModel)
def get_calling_status():
    return {"id": CallingStatus.id,"message": CallingStatus.message,"type":CallingStatus.type}

@app.get("/status",response_model=StatusResponseModel)
def get_status():
    return {"message":GSMStatus.message,"error":GSMStatus.is_error}

@app.post("/call-sequence",response_model=CallSequenceResponseModel)
async def call_sequence(background_task: BackgroundTasks):
    if CallingStatus.is_call_active==True:
        return {
            "is_free": False,
        }
    else:
        background_task.add_task(emergency_process)
        return {
            "is_free": True
        }

@app.get("/")
async def index():
    return RedirectResponse(url="/static")

# app.mount("/",StaticFiles(directory="static/",html=True),name="static")
if __name__ == "__main__":
    uvicorn.run(app,port=8000,host="0.0.0.0")




