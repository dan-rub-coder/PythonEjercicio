import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ('dcrubiano01@gmail.com', 'Poiuytrewq-123')

    response = session.get(url)
    
    if response.ok:
        response = session.get('https://github.com/dan-rub-coder')
        if response.ok:
            print(response.cookies)

