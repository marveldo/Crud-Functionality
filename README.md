
# An Api capable of CRUD(create read update delete) functionalities on a persons data

A brief description on how the api can be used

## 
#### Create Profile
```http
  GET /api
```

#### Request
```http
  data = {"name": "anyname"}
  requests.post(f'https://crud-functionality-hqud.onrender.com/api/{id}/',json = data)

```
#### Response
```http
  data = {"name": "anyname","id": "A given id"}
```
#### Get Profile

```http
  GET /api/id/
```

| Parameter | Type     | METHOD                      |
| :-------- | :------- | :-------------------------------- |
| `id`      | ` Integer` | GET |

#### Request
```http
  data = {"name": "anyname"}
  requests.get(f'https://crud-functionality-hqud.onrender.com/api/{id}/')

``` 
#### Response
```http
  data = {"name": "anyname","id": "id passed into it"}
```

#### Update Profile

```http
  PUT /api/id/
```

| Parameter | Type     | METHOD                      |
| :-------- | :------- | :-------------------------------- |
| `id`      | ` Integer` | PUT |

#### Request
```http
  data = {"name": "Updated name"}
  requests.put(f'https://crud-functionality-hqud.onrender.com/api/{id}/',json = data)

```
#### Response
```http
  data = {"name": "Updated name","id": "id passed into it"}

```
#### Delete Profile

```http
  PUT /api/id/
```

| Parameter | Type     | METHOD                      |
| :-------- | :------- | :-------------------------------- |
| `id`      | ` Integer` | Delete |

#### Request
```http
  requests.delete(f'https://crud-functionality-hqud.onrender.com/api/{id}/')

```
#### Response
```http
  Succesfully deleted
```
## Testing


for the test script visit https://github.com/marveldo/Crud-Functionality/blob/main/test.py
for Validation used in the development of the api visit https://github.com/marveldo/Crud-Functionality/blob/main/api/views.py

## UML REPRESENTATION

![UML Diagram](https://github.com/marveldo/Crud-Functionality/blob/main/UML%20diagram%20for%20database.png)

## Deployment

Project was succesfully deployed to render with 

the live file being https://crud-functionality-hqud.onrender.com/api

firstly i commited the project to github then went over to render to host directly from github 

it required downloading the requirements.txt file with pip install -r requirements.txt and then gunicorn was needed for the execution of the file 

##Challenges and limitation
Authentication methods not used


The data cannot be queried from the name more from the id


