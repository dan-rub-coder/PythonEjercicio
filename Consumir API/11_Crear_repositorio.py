#https://github.com/login/oauth/authorize?client_id=683b35ea01ddb41d224f&scope=repo


import requests

if __name__ == '__main__':
    client_id = '683b35ea01ddb41d224f'
    client_secret = '7f724c421b412f15fbe7b1d0b4563967eebae9e7'
    code = 'e1c3a6faf1d2d9751ff3'
    access_token = '294f81a31c6fb06363eaa2ba5f2bc8f44532e9ef'

    url ='https://api.github.com/user/repos'
    paylod = {'name':'git_hub_cf_comunidad'}
    headers = {'Accept':'application/vnd.github.nebula-preview+json', 'Autorization':'token'+ access_token, }

    response = requests.post(url, headers=headers, json=paylod)

    if response.status_code == 200:
        print(response.json() )
    else:
        print(response.content)