import requests as req
import json


head = {"Content-Type": "application/json"}
base = "http://127.0.0.1:5000/api/v1/login"
data = {"email": "fake2", "password":"fake2",
        "username": "fake2"}
with req.post(base, headers=head,
              data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())
    auth = marko.cookies.get("Auth")

data = {"title": "Title with auther4", "content": "Some text4",
        "tags": ["new", "test", "username"], "status": "draft"}
base = "http://127.0.0.1:5000/api/v1/add_article"
sess = req.Session()
sess.cookies.set("Auth", auth)
with sess.post(base, headers=head,
               data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())

data = {"title": "Title with auther5", "content": "Some text5",
        "tags": ["new", "test", "username"], "status": "published"}
base = "http://127.0.0.1:5000/api/v1/add_article"
sess = req.Session()
sess.cookies.set("Auth", auth)
with sess.post(base, headers=head,
               data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())

data = {"title": "Title with auther1", "content": "Some text1",
        "tags": ["new", "test", "username"], "status": "published"}
base = "http://127.0.0.1:5000/api/v1/add_article"
sess = req.Session()
sess.cookies.set("Auth", auth)
with sess.post(base, headers=head,
               data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())

data = {"title": "Title with auther5", "content": "Some text5",
        "tags": ["new", "test", "username"], "status": "draft"}
base = "http://127.0.0.1:5000/api/v1/add_article"
sess = req.Session()
sess.cookies.set("Auth", auth)
with sess.post(base, headers=head,
               data=json.dumps(data)) as marko:
    print(marko.status_code)
    print(marko.json())

base = "http://127.0.0.1:5000/api/v1/articles"
sess = req.Session()
sess.cookies.set("Auth", auth)
with sess.get(base, headers=head) as marko:
    print(marko.status_code)
    print(marko.json())
    ID = marko.json().get("articles")[0].get("db ID")
    print("chosen ID is: " + ID)
    print("\n")

base = "http://127.0.0.1:5000/api/v1/articles/" + ID
sess = req.Session()
sess.cookies.set("Auth", auth)
with sess.get(base, headers=head) as marko:
    print(marko.status_code)
    print(marko.json())

base = "http://127.0.0.1:5000/api/v1/articles/search_articles"
sess = req.Session()
search = {"q": {"title": "new Title"}}
sess.cookies.set("Auth", auth)
with sess.get(base, headers=head,
              params=search) as marko:
    print(marko.status_code)
    print(marko.json())
