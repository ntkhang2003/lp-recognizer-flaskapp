from flask import Flask, render_template, request
from detection import detection
from recognition import recognition
from io import BytesIO
import numpy as np
import cv2
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    # try:
    imagefile = request.files['imagefile']
    img_bytes = imagefile.read()
    # Chuyển dữ liệu ảnh thành mảng NumPy sử dụng OpenCV
    nparr = np.frombuffer(img_bytes, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    image_data = base64.b64encode(img_bytes).decode('utf-8')
    if (request.form.get('detection')):
        cropped_img = detection(request.form.get('detection'), img_np)
        prediction = recognition(request.form.get('recognition'), cropped_img)
        return render_template('index.html', detection = request.form.get('detection'), recognition = request.form.get('recognition'), prediction = prediction, image_data = image_data)
    # except:
    #     return render_template('index.html', prediction = 'Error occurred')