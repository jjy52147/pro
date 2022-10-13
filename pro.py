import requests
import json

def test_channel():
    url = "http://8.219.83.66:8088/admin/v2/login"
    
    login = '{"username": "admin", "password": "1234"}'
    # login = '{"password":"1234","username":"admin"}'
    
    header = {"Content-Type": "application/json"}
    
    r = requests.post(url, data = login, headers = header)

    
    #print(r.json())
    #print(r.text)

    url = "http://8.219.83.66:8088/admin/v2/system/dict/data/channels"

    login = '{"pageSize": "10000", "pageNum": "1"}'

    header = {
        "Content-Type": "application/json",
        "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImJjZWVhOGI0LTI5NjktNGM3MS1iOGVjLTEwOTA5NzJhNTUyYiJ9.3lrG37laL7iw3qbPULK-BRl_Ba4i5u68QvBtD58b8v5ffdP9vYEVmVIPyachn18hV-ogCWwlL0IOFWoKSAsrPw"
        }

    r = requests.post(url, data = login, headers = header)

    print(r.text)

    

if __name__ == "__main__":
    test_channel()
    
