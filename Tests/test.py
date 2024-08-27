import requests as req
import json


ID = "66c4e2dd0654664cbab78f2c"
base = "http://127.0.0.1:5000/api/v1/login"
head = {"Content-Type": "application/json"}
data = {"username": "fake2", "email": "fake2",
        "password": "fake2"}
with req.post(base, headers=head,
              data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())
    auth = marko.cookies.get("Auth")

data = {"username": "newuser2", "email": "mega2@email.com",
        "password": "password2"}
base = "http://127.0.0.1:5000/api/v1/edit_user/" + ID
sess = req.Session()
sess.cookies.set("Auth", auth)
with sess.put(base, headers=head,
              data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())
#base = "http://127.0.0.1:5000/api/v1/edit_user/"
#with req.get(base, headers=head) as marko:
#    print(marko.json())
#    print(marko.status_code)
