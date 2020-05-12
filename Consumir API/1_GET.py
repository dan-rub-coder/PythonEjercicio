import requests

if __name__ == '__main__':
    url='https://www.google.com.co/'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        file = open("goole.txt", 'wb')
        file.write(content)
        file.close()
