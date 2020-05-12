import requests
import json


if __name__ == '__main__':
    url='http://httpbin.org/post'
    payload = {'Nombre':'Daniel', 'Curso':'Python', 'nivel':'Intermedio'}
    
    response = requests.post(url, data=json.dumps(payload))
    print(response.url)

#Al enviar los datos a data estos se enviaran automaticamene al form
#por eso hay que serializarlos para enviarlos como json.dumps()

#json post se encarga de serializarlos
#data entonces nosotros serializamos

    if response.status_code == 200:
        print(response.content)