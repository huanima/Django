import requests
import pprint



payload = {
    'username': 'huanima',
    'password': 'Hejingyi'
}

response = requests.post('http://127.0.0.1/api/mgr/signin',
                         data=payload)

# print(response)
pprint.pprint(response.json())
# pprint.pprint(response.json().decode())