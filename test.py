import requests

name1 = 'Marvelous'
name2 = 'John'

# testing Create
url = f'https://crud-functionality-hqud.onrender.com/api'
data = {'name': name1}

response = requests.post(url,json=data)
data = response.json()
print(f"Your data has been created it is {data}")


# function to test GET request
def get(id):
    url3 = f'https://crud-functionality-hqud.onrender.com/api/{id}'
    response = requests.get(url3)
    print(f"Here is your data {response.text}")
    

get(int(data['id']))

# function to test PUT request
def update(id,name):
    url5 = f'https://crud-functionality-hqud.onrender.com/api/{id}'
    data = {'name': name}
    
    response = requests.put(url5, json= data)

    print(f"your data has been updated to {response.text}")

update(int(data['id']), name2)

# function to test DELETE request
def delete(id):
    url4 = f'https://crud-functionality-hqud.onrender.com/api/{id}'

    response = requests.delete(url4)

    print("Your data has been removed")
    

delete(data['id'])

