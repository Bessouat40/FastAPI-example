import requests

data = {'number' : 1}

response = requests.post('http://localhost:8000/soustraction', data = data)

print('------------------')
print('API response : ', response.json())
print('------------------')