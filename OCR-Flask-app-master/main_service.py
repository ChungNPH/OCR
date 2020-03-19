import os,cv2,pytesseract
from flask import Flask, render_template, request, jsonify
from PIL import Image
from tesseract import ocr

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'

app = Flask(__name__)

@app.route('/api/ocr/<string:d>', methods=['POST','GET'])
def upload_file(d):
    if request.method == "GET":
        return "This is the api BLah blah"
    elif request.method == "POST":
        # d = request.get_json()
        # user_name = d['user_name']
        # pw = d['password']
        # user_pics = d['user_pics']
        # results = ocr(user_pics)
        return jsonify({"user_name" : request.params, "pw" : request.params, "user_pics" : request.file})

app.run("0.0.0.0",5000,threaded=True,debug=True)