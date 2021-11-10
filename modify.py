from requests import patch
from secrets import token_urlsafe
from os.path import isfile

if not isfile('id.secret'):
    print('Message ID not found.')
    exit(1)

with open('id.secret', 'r') as file:
    m_id = file.read()

if not isfile('token.secret'):
    print('token not found.')
    exit(1)

with open('token.secret', 'r') as file:
    token = file.read()

r = patch(f'{token}/messages/{m_id}?wait=true',
          json={'content': f'https://2buldzha2t.ru/donaters.gif?token={token_urlsafe(16)}'})

if r.status_code != 200:
    print('Error.', r.text)
    exit(1)
