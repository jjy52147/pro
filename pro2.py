import requests
import json

def test_channel():
    url = "http://8.219.83.66:8088/admin/v2/login"
    
    login = '{"username": "admin", "password": "1234"}'
    
    # login = '{"password":"1234","username":"admin"}'
    
    header = {
        "Content-Type": "application/json",
        #"Cookie": "eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjczN2I4YmRjLTJhYWMtNDY4OC04ZDE4LWFhMzgyMDk0Y2NkZSJ9.-HXq9_7IRugcpUsdxOIeEYk7DKDbF0ifmiP3kT-ia8JBo8ogeTpQ7auuKjjG6fXoUGclXBrPq-9UNA-SB8Yd0g"
        }
    
    r = requests.post(url, data = login, headers = header)

    #token1 = r. json(). get("data"). get("token")

    #token = r.json()

    #return token["r"]
    
    
    
    a = json.loads(r.text)

    token1 = a["token"]

    print(token1)

    
    #print(r.json())
    #print(r.text)

    url = "http://8.219.83.66:8088/admin/v2/system/dict/data/channels"

    login = '{"pageSize": "10000", "pageNum": "1"}'

    header = {
            "Content-Type": "application/json", 
            "Authorization": token1 
            }

    r = requests.post(url, data = login, headers = header)

    print(r.text)

    

    

if __name__ == "__main__":
    test_channel()
    
#   p r o  
 