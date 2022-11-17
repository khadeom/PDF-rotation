import requests
BASE = "http://127.0.0.1:5000/"

def test_post():

    response  = requests.post(BASE+"pdf/6",{"filePath":'VRP.pdf',"angleOfRotation":90,'number':2})
    print(response.json())
    assert response.status_code == 200
    assert response.json()["outputPath"]== 'tmp/test_VRP.pdf'
    assert response.json()["id"] == 6
    assert response.json()["angleOfRotation"] == 90
    assert response.json()["number"] == 2

def test_get():
    output = requests.get(BASE+"pdf/6")
    print(output.json())

    assert output.status_code == 200
    assert output.json()["outputPath"]== 'tmp/test_VRP.pdf'
    assert output.json()["id"] == 6
    assert output.json()["angleOfRotation"] == 90
    assert output.json()["number"] == 2


