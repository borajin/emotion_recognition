# live_streaming.py

from flask import Flask, render_template, Response
import emotion_recog

import os
import socket
import threading
import json
import time

app = Flask(__name__)
server_address =  ('127.0.0.1', 4444)

d = None

@app.route('/')
def index():
    return render_template('index.html')

def launch_socket_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    while True:
        data, addr = sock.recvfrom(200)
        d = data.decode()
        #if d["is"] == "smile":
        #    f = open('smile.txt', 'w')
        #    f.write(d)
        #    f.close()
        #else:
        f = open('result.json', 'w')
        f.write(d)
        f.close()

def r():
    while True:
        time.sleep(1)
        with open('result.json', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
        
        return json_data["big_emotion"] + "," + str(json_data["angry"]) + "," + str(json_data["disgust"]) + "," + str(json_data["scared"]) + "," + str(json_data["happy"]) + "," + str(json_data["sad"]) + "," + str(json_data["surprised"]) + "," + str(json_data["neutral"])

@app.route('/result')
def result():
    return Response(r())

def s():
    f = open('smile.txt', 'r')
    jpg_bytes = f.read()
    yield (b'--frame\r\n'
          b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

@app.route('/smile')
def smile():
    return Response(s(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    t = threading.Thread(target=launch_socket_server)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=7777, debug=True)
