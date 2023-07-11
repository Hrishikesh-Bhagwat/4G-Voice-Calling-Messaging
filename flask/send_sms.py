from serial import Serial
import time
from pygame import mixer
import os
from datetime import datetime

def play_clip(path):
    if os.path.exists(path):
        mixer.init()
        mixer.music.load(path)
        mixer.music.play()
        while mixer.music.get_busy():
            continue

def make_call_handler(phone,pairs):
    port="/dev/ttyS0"
    ser=Serial(port,baudrate=115200,timeout=20)
    # ser.write(b"AT\r\n")
    # time.sleep(1.2)
    # ser.readall()
    # ser.write(b"AT\r\n")
    ser.reset_output_buffer()
    ser.reset_input_buffer()
    ser.write("AT\r\n".encode('utf-8'))
    c=0
    time.sleep(4)
    while True:
        c+=1
        if c>150:
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            ser.close()
            return {
                "status": False,
                "message":"Modem unresponsive"
            }
        a=ser.readline()
        print(a)
        if "OK" in a.decode('utf-8'):
            break
    ser.write(f"ATD+91{phone};\r\n".encode('utf-8'))
    start=datetime.now()
    c=0
    while True:
        c+=1
        if c>150:
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            ser.close()
            return {
                "status": False,
                "message":"Modem unresponsive"
            }
        a=ser.readline()
        print(a)
        if "BEGIN" in a.decode('utf-8'):
            break
        if "NO CARRIER" in a.decode('utf-8') or (datetime.now()-start).total_seconds()>30:
            ser.write("AT+CHUP\r\n".encode('utf-8'))
            while True:
                c+=1
                if c>150:
                    ser.reset_output_buffer()
                    ser.reset_input_buffer()
                    ser.close()
                    return {
                        "status": False,
                        "message":"Modem unresponsive"
                    }
                a=ser.readline()
                print(a)
                if "OK" in a.decode('utf-8'):
                    break
            
            return {
                "status": False,
                "message": "Call not received"
            }
    for i in pairs:
        play_clip(i["heading"])
        play_clip(i["entry"])
    
    time.sleep(2)
    ser.write("AT+CHUP\r\n".encode('utf-8'))
    c=0
    while True:
        c+=1
        if c>150:
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            ser.close()
            return {
                "status": False,
                "message":"Modem unresponsive"
            }
        a=ser.readline()
        print(a)
        if "OK" in a.decode('utf-8'):
            break
    ser.reset_output_buffer()
    ser.reset_input_buffer()
    ser.close()
    return {
        "status": True,
        "message":"Placed call successfully!"
    }
    

def send_sms(phone,message):
    port="/dev/ttyS0"
    ser=Serial(port,baudrate=115200,timeout=20)
    ser.reset_output_buffer()
    ser.reset_input_buffer()
    ser.write("AT\r\n".encode('utf-8'))
    time.sleep(4)
    while True:
        a=ser.readline()
        print(a)
        if "OK" in a.decode('utf-8'):
            break
    print("Initialized :)")
    ser.write(b'AT+CMGF=1\r\n')
    c=0
    while True:
        a=ser.readline()
        if "OK" in a.decode('utf-8'):
            break
        c+=1
        if c>15:
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            ser.close()
            return {
                "status": False,
                "message":"Module not functioning"
            }
    
    c=0
    ser.write((f'AT+CMGS="{phone}"\r\n').encode('utf-8'))
    time.sleep(10)
    while True:
        a=ser.readline()
        if ">" in a.decode('utf-8'):
            break
        c+=1
        if c>15:
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            ser.close()
            return {
                "status":False,
                "message":"Module not functioning"
            }

    c=0
    ser.write((f'{message}\r\n\x1A').encode('utf-8'))
    time.sleep(5)
    while True:
        a=ser.readline()
        if "+CMS ERROR" in a.decode('utf-8'):
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            ser.close()
            return {
                "status": False,
                "message":"An error occurred in sending message"
            }

        if "OK" in a.decode('utf-8'):
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            ser.close()
            return {
                "status": True,
                "message":"Sent message successfully"
            }

        c+=1
        if c>15:
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            ser.close()
            return {
                "status": False,
                "message": "An error occurred in sending message"
            }
