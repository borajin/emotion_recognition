# emotion_recognition

### 참고
https://appliedmachinelearning.blog/2018/11/28/demonstration-of-facial-emotion-recognition-on-real-time-video-using-cnn-python-keras/
https://github.com/omar178/Emotion-recognition

### 환경
```
python==3.6.5
NAVIDA GPU DRIVER (각자 컴퓨터 그래픽카드에 맞춰서...)
CUDA 9.0
CUDNN 7.6.4v for CUDA 9.0
virturalenv 사용
```

#### virtualenv
```
pip install virtualenv
virtualenv myenv
myenv\Scripts\activate
(myenv) ~ /c:...
```

### requirements
```
pip install opencv-python
pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl
pip install cmake
pip install face-recognition
pip install flask
pip install tensorflow-gpu==1.12
pip install keras
pip install imutils
```

2번째 whl 파일은 각자 운영체제에 맞는 것으로

### 실행법
1번째 창
```
(myenv) python server.py
```
2번째 창
```
(myenv) python streaming_server.py
```
localhost:7777 접속
