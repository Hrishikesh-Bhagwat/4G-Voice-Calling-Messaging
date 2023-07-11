from doctest import debug
from flask import Flask, jsonify, request
from flask_cors import CORS
import time
from serial import Serial
from send_sms import send_sms as send_sms_handler, make_call_handler
app = Flask(__name__)

port="/dev/ttyS0"

CORS(app)
res={
    "message":"All Good!",
    "is_error":False
}
# Define a route and a view function
@app.route('/diagnostics')
def check_diagnostics():
    try:
        # check signal strength
        ser=Serial(port,baudrate=115200,timeout=15);ser.reset_output_buffer()
        ser.write(b"AT\r\n")
        time.sleep(1.2)
        ser.readall()
        ser.write(b"AT\r\n")
        c=0
        while True:
            c+=1
            a=ser.readline()
            if len(a.decode('utf-8'))==0:
                ser.reset_output_buffer()
                ser.reset_input_buffer()
                ser.close()
                return jsonify({
                    "message":"Modem unresponsive. Working to reset...",
                    "is_error":True
                })
            if "OK" in a.decode('utf-8'):
                break
            if c>50:
                ser.reset_output_buffer()
                ser.reset_input_buffer()
                ser.close()
                return jsonify({
                    "message":"An unknown error occurred",
                    "is_error":True
                })
        
        c=0
        ser.write(b"AT+CSQ\r\n")
        while True:
            c+=1
            a=ser.readline()
            if len(a.decode('utf-8'))==0:
                ser.reset_output_buffer()
                ser.reset_input_buffer()
                ser.close()
                return jsonify({
                    "message":"Modem unresponsive. Working to reset...",
                    "is_error":True
                })
            if "+CSQ:" in a.decode('utf-8'):
                ser.reset_output_buffer()
                ser.reset_input_buffer()
                ser.close()
                if "99" in a.decode('utf-8'):
                    return jsonify({
                        "message":"Weak network",
                        "is_error": True
                    })
                else:
                    break
            if c>50:
                ser.reset_output_buffer()
                ser.reset_input_buffer()
                ser.close()
                return jsonify({
                    "message":"An unknown error occurred",
                    "is_error":True
                })

        c=0
        ser.write(b"AT+CPIN?\r\n")
        while True:
            c+=1
            a=ser.readline()
            if len(a.decode('utf-8'))==0:
                ser.reset_output_buffer()
                ser.reset_input_buffer()
                ser.close()
                return jsonify({
                    "message":"Modem unresponsive. Working to reset...",
                    "is_error":True
                })
            if "+CPIN:" in a.decode('utf-8'):
                if "READY" in a.decode('utf-8'):
                    ser.reset_output_buffer()
                    ser.reset_input_buffer()
                    ser.close()
                    return jsonify({
                        "message":"All good",
                        "is_error": False
                    })
                else:
                    ser.reset_output_buffer()
                    ser.reset_input_buffer()
                    ser.close()
                    return jsonify(
                        {
                            "message":"SIM not ready",
                            "is_error": True
                        }
                    )
            if c>50:
                ser.reset_output_buffer()
                ser.reset_input_buffer()
                ser.close()
                return jsonify({
                    "message":"An unknown error occurred",
                    "is_error":True
                })
        # check SIM
    except Exception as e:
        return jsonify({"message":"An unknown error occurred!","is_error":True})
    
@app.route("/send-sms",methods=["POST"])
def send_sms():
    request_body=request.json
    text=request_body["text"]
    number=request_body["phone"]
    send_sms_status=send_sms_handler(number,text)
    return jsonify(send_sms_status)

@app.route("/make-call",methods=["POST"])
def make_call_route():
    request_body=request.json
    pairs=request_body["pairs"]
    number=request_body["phone"]
    make_call_status=make_call_handler(number,pairs)
    return jsonify(make_call_status)


@app.route('/trigger-emergency',methods=["POST"])
def make_call():
    time.sleep(200)
    return {
        "status":"error",
        "message":"Call not answered!"
    }

# Run the application if this script is executed
if __name__ == '__main__':
    app.run(port=5000, debug=True)