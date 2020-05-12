import requests

#En args vamos a encontrar los parametros que le 
#hayamos enviado al servidor

"""
if __name__ == '__main__':
    url = 'http://httpbin.org/get?nombre=daniel&curso=python'
    response = requests.get(url)
#De esta forma se podria enviar parametros por medio de la URL pero no es la forma mas obtima
"""


if __name__ == '__main__':
    url='http://httpbin.org/get'
    args = {'Nombre':'Daniel', 'Curso':'Python', 'nivel':'Intermedio'}
    response = requests.get(url, params=args)
    print(response.url)


    if response.status_code == 200:
        content = response.content 
        print(content)

