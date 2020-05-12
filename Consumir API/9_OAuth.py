#API de GitHub
#Practica

#https://developer.github.com/v3/oauth/

import requests
client_id = '683b35ea01ddb41d224f'
client_secret = '7f724c421b412f15fbe7b1d0b4563967eebae9e7'

#https://github.com/login/oauth/authorize?client_id=683b35ea01ddb41d224f&scope=repo

code = '64b4f9b8f5cf12184646'
#access_token = '294f81a31c6fb06363eaa2ba5f2bc8f44532e9ef'

#Con el code, client_id y client_secret voy a tener un Acces_token 
#El acces_token es un string alfanumerico que permitira realizar diferentes peticiones para tener diferentes recurso
#del usuario(imagen de perfil, nombre completo, donde trabaja)


if __name__ == '__main__':
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id':client_id, 'client_secret':client_secret, 'code':code}#Parametros requeridos que exige la url
    headers = {'Accept': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)


    if response.status_code == 200:
        response_json = response.json()
        print(response_json)

        access_token = response_json['access_token']
        print(access_token)
        