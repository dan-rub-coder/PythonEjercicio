
import requests

client_id = '683b35ea01ddb41d224f'

client_secret = '7f724c421b412f15fbe7b1d0b4563967eebae9e7'

#https://github.com/login/oauth/authorize?client_id=683b35ea01ddb41d224f&scope=repo

code = 'e1c3a6faf1d2d9751ff3'
access_token = '294f81a31c6fb06363eaa2ba5f2bc8f44532e9ef'

if __name__ == '__main__':
    url = 'https://developer.github.com/v3/repos/'
    headers = {'Accept':'application/vnd.github.nebula-preview+json' }

    params = {'Autorization':'token'+ access_token}
    response = requests.get(url, headers=headers, params=params)
    print(response)
    if response.status_code == 200:
        payload = response.content
        print(payload)
        #print(payload)

        #for project in payload:
         #   name = project['name']
          #  print('name')
    else:
        print(response.content)
        
#https://developer.github.com/v3/repos/#get