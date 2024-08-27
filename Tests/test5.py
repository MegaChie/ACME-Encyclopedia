import requests as req
import json
import time


base = "http://18.210.10.89:5000/translate"
head = {"Content-Type": "application/json"}
text = {"q": ["he is making food", "i think he is handsome"], "source": "en",
        "target": "ar"}
start = time.time()
with req.post(base, headers=head,
              data=json.dumps(text)) as marko:
    print(marko.status_code)
    print(marko.json())
end = time.time()
print("took {} sec".format(end - start))
