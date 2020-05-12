import requests 
import json

if __name__ == '__main__':
    url = 'https://upload.wikimedia.org/wikipedia/commons/6/69/NASA-HS201427a-HubbleUltraDeepField2014-20140603.jpg'
    
    response = requests.get(url, stream=True)#Realiza la peticion sin descargar el contenido. El stream True no cierra la conexion
    with open('image.jpg','wb') as file:
        for chunk in response.iter_content():#Descarga el contenido poco a poco
          file.write(chunk) 

    response.close()