import os,cv2,pytesseract
from flask import Flask, render_template, request, jsonify
from PIL import Image
from tesseract import ocr

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/ocr/<string:d>', methods=['POST','GET'])
def upload_file(d):
    if request.method == "GET":
        return "This is the api BLah blah"
    elif request.method == "POST":
        file = request.files['image']

        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
        file.save(f)
        print(file.filename)

        image = cv2.imread(UPLOAD_FOLDER+"/"+file.filename)
        os.remove(UPLOAD_FOLDER+"/"+file.filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

app.run("0.0.0.0",5000,threaded=True,debug=True)


