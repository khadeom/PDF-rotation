import requests
BASE = "http://127.0.0.1:5000/"

def test_main():

    response  = requests.post(BASE+"pdf/3",{"filePath":'VRP.pdf',"angleOfRotation":90,'number':2})
    print(response.json())
    assert response.status_code == 200
    assert response.json()["filePath"]== 'VRP.pdf'
    assert response.json()["id"] == 3
    assert response.json()["angleOfRotation"] == 90
    assert response.json()["number"] == 2

def test_get():
    output = requests.get(BASE+"pdf/3")
    print(output.json())

    assert output.status_code == 200
    assert output.json()["outputPath"]== 'tmp/test.pdf'
    assert output.json()["id"] == 3
    assert output.json()["angleOfRotation"] == 90
    assert output.json()["number"] == 2


