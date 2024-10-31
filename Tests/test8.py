import requests as req
import json


head = {"Content-Type": "application/json"}
base = "http://54.157.134.146:5000/api/v1/login"
data = {"email": "fake2", "password":"fake2",
        "username": "fake2"}
with req.post(base, headers=head,
              data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())
