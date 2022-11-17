import requests

BASE = "http://127.0.0.1:5000/"

response  = requests.post(BASE+"pdf/4",{"filePath":'VRP.pdf',"angleOfRotation":90,'pageNumber':2})
if response.status_code == 409:
    print(response.json().get("message"))
else:
    print(response.json())

output = requests.get(BASE+"pdf/4")
print(output.json())