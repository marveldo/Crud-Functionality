import requests

name = input('  Enter your name')
url = f'http://127.0.0.1:8000/api'
data = {'name': name}

response = requests.post(url,json=data)
print(response.text)

def get(id):
    url3 = f'http://127.0.0.1:8000/api/{id}/'
    response = requests.get(url3)
    print(response.text)

get(int(input("enter your id")))

def update(id,name):
    url5 = f'http://127.0.0.1:8000/api/{id}/'
    data = {'name': name}
    response = requests.put(url5, json= data)
    print(response.text)

update(int(input("enter your id")), input("enter the new name"))

def delete(id):
    url4 = f'http://127.0.0.1:8000/api/{id}/'
    response = requests.delete(url4)
    print(response.text)

delete(int(input("Enter your id")))

