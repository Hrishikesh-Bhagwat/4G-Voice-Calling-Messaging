from queue import Queue
from threading import Thread
from datetime import datetime, timedelta

class GSMStatus:
    message="Unknown State"
    is_error=True
    last_updated=datetime.now()

class CallingStatus:
    is_call_active=False
    message=""
    type=""
    id=""

def gsm_activity_thread(queue: Queue):
    while True:
        if GSMStatus.last_updated==None:
            #update status
            #update time
            pass
        now=datetime.now()
        fifteen_seconds = timedelta(seconds=15)
        if now-GSMStatus.last_updated>=fifteen_seconds:
            #update status
            #update time
            pass

        if queue.not_empty:
            top=queue.get()
            # handle sms request
            # handle call request
