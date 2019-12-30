import requests
import json

from sklearn.datasets import load_boston
data,target = load_boston().data,load_boston().target

url = 'http://localhost:5000/api'
json_data = json.dumps({ i:v for i,v in enumerate(data[0]) })
r = requests.post(url, data=json_data)
print(r,r.text)