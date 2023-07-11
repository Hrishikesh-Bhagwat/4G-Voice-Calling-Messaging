from serial import Serial
from utils.path_utils.paths import ser_path

def diagnostics_check():
    try:
        # check signal strength
        ser=Serial(ser_path,baudrate=115200,timeout=15)
        ser.write(b"AT\r\n")
        c=0
        while True:
            c+=1
            a=ser.readline()
            if len(a.decode('utf-8'))==0:
                return {
                    "message":"4G Module unresponsive",
                    "is_error":True
                }
            if "OK" in a.decode('utf-8'):
                break
            if c>50:
                return {
                    "message":"An unknown error occurred",
                    "is_error":True
                }
        
        c=0
        ser.write(b"AT+CSQ\r\n")
        while True:
            c+=1
            a=ser.readline()
            if len(a.decode('utf-8'))==0:
                return {
                    "message":"4G Module unresponsive",
                    "is_error":True
                }
            if "+CSQ" in a.decode('utf-8'):
                if "99" in a.decode('utf-8'):
                    return {
                        "message":"Weak network",
                        "is_error": True
                    }
                else:
                    break
            if c>50:
                return {
                    "message":"An unknown error occurred",
                    "is_error":True
                }

        c=0
        ser.write(b"AT+CPIN?\r\n")
        while True:
            c+=1
            a=ser.readline()
            if len(a.decode('utf-8'))==0:
                return {
                    "message":"4G Module unresponsive",
                    "is_error":True
                }
            if "+CPIN" in a.decode('utf-8'):
                if "READY" in a.decode('utf-8'):
                    return {
                        "message":"All good",
                        "is_error": False
                    }
                else:
                    return {
                        "message":"SIM not ready",
                        "is_error": True
                    }
            if c>50:
                return {
                    "message":"An unknown error occurred",
                    "is_error":True
                }
        # check SIM
    except Exception as e:
        return {"message":"An unknown error occurred!","is_error":True}