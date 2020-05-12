import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/cookies'
    cookies = {'my-cookie' : 'true'}

    response = requests.get(url, cookies=cookies)

    if response.ok:  #puede usarse el 200 o ok 
        cookies = response.cookies
        print(cookies)

        print('el contenido es: ')
        print(response.content)