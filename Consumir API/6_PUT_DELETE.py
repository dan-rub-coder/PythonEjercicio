import requests
import json


if __name__ == '__main__':
    url='http://httpbin.org/put'
    #url='http://httpbin.org/delete'
    payload = {'Nombre':'Daniel', 'Curso':'Python', 'nivel':'Intermedio'}
    #response = requests.delete(url, data=json.dumps(payload))
    response = requests.put(url, data=json.dumps(payload))
    print(response.url)

    if response.status_code == 200:
        headers_response = response.headers #Diccionario
        server = headers_response['Server']
        print(server)