import requests as req
import json


head = {"Content-Type": "application/json"}
base = "http://127.0.0.1:5000/api/v1/login"
data = {"email": "fake2", "password": "fake2",
        "username":"fake2"}
with req.post(base, headers=head,
              data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())
    auth = marko.cookies.get("Auth")


base = "http://127.0.0.1:5000/api/v1/articles"
sess = req.Session()
sess.cookies.set("Auth", auth)
with sess.get(base, headers=head) as marko:
    print(marko.status_code)
    print(marko.json())
    ID = marko.json().get("articles")[0].get("db ID")
    print("\n")
    print("article ID is: " + ID)


base = "http://127.0.0.1:5000/api/v1/edit_articles/" + ID
sess = req.Session()
sess.cookies.set("Auth", auth)
data = {"name": "Edited", "content": "New text"}
with sess.get(base, headers=head,
              data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())


base = "http://127.0.0.1:5000/api/v1/articles"
sess = req.Session()
sess.cookies.set("Auth", auth)
with sess.put(base, headers=head) as marko:
    print(marko.status_code)
    print(marko.json())
