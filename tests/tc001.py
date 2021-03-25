import requests
import pprint



payload = {
    'username': 'huanima',
    'password': 'Hejingyi'
}

response = requests.post('http://127.0.0.1:80/api/mgr/signin',
                         data=payload)

pprint.pprint(response.json())
