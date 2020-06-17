from flask import Flask, render_template, Response
import emotion_recog

app = Flask(__name__)

def gen(fr):
    while True:
        jpg_bytes = fr.get_jpg_bytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

@app.route('/')
def video_feed():
    return Response(gen(emotion_recog.EmotionRecog()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)