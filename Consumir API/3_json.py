import requests
import json


if __name__ == '__main__':
    url='http://httpbin.org/get'
    args = {'Nombre':'Daniel', 'Curso':'Python', 'nivel':'Intermedio'}
    response = requests.get(url, params=args)
    print(response.url)


    if response.status_code == 200:

        response_json = response.json() #Diccionario
        origin = response_json['origin']#De esta forma puedo solicitar un valor especifico en el json()
        print(origin)

"""
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)
"""

#De estas dos formas solicitamos los valores de 'origin' que se encuentra dentro del json()
#de igual forma se usa para los otros valores 