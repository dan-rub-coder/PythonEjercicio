import requests
import json


if __name__ == '__main__':
    url='http://httpbin.org/post'
    payload = {'Nombre':'Daniel', 'Curso':'Python', 'nivel':'Intermedio'}
    headers = {'Conten-Type':'application/json', 'access-token':'12345'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)

#Para leer los encabezados
    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers #Diccionario
        #print(headers_response)
        server = headers_response['Content-Length']
        print(server)