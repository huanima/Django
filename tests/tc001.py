import requests,pprint

payload = {
    'userName': 'huanima',
    'password': 'Hejingyi'
}

response = requests.post('http://localhost/api/mgr/signin',
                         data=payload)

pprint.pprint((response.json()))