from requests import post
from secrets import token_urlsafe
from os.path import isfile


if not isfile('token.secret'):
    print('token not found.')
    exit(1)

with open('token.secret', 'r') as file:
    token = file.read()

r = post(f'{token}?wait=true',
         json={'content': f'https://2buldzha2t.ru/donaters.gif?token={token_urlsafe(16)}'})

content = r.json()

with open('id.secret', 'w') as file:
    file.write(content['id'])

if r.status_code != 200:
    print('Error.', r.text)
    exit(1)
