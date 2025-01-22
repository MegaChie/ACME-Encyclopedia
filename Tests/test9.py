import requests as req
import json


head = {"Content-Type": "application/json"}
base = "http://localhost:5000/api/v1/"
data = {"email": "fake2", "password":"fake2",
        "username": "fake2"}
with req.post(base + "login", headers=head,
              data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())
    auth = marko.cookies.get("Auth")

log = {"Auth": auth}

with req.get(base + "auth_check", headers=head, cookies=log) as marko:
    print(marko.status_code)
    print(marko.json())

log = {"Auth": "asfdg976adgASGdsgtseG4"}
with req.get(base + "auth_check", headers=head, cookies=log) as marko:
    print(marko.status_code)
    print(marko.json())

