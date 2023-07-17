from flask import Flask, render_template, request
from detection import detection
from recognition import recognition

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    # try:
    imagefile = request.files['imagefile']
    img_path = "./static/" + imagefile.filename
    imagefile.save(img_path)
    
    if (request.form.get('detection')):
        cropped_img = detection(request.form.get('detection'), img_path)
        prediction = recognition(request.form.get('recognition'), cropped_img)
        return render_template('index.html', detection = request.form.get('detection'), recognition = request.form.get('recognition'), prediction = prediction)
    # except:
    #     return render_template('index.html', prediction = 'Error occurred')

if __name__ == '__main__':
    app.run(port = 3000, debug = True)