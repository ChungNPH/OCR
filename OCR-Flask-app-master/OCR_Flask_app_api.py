# can use request module
import requests
import sys

def call_api():
    api = "http://localhost:5000/api/ocr"
    files = {'image': open('./images/car_wash.png', 'rb')}

    params = {"user_name" : "user_name", "password": "password"}
    print(requests.post(api,params,files=files).text)

if __name__ == '__main__':
    call_api()