
# An Api capable of CRUD(create read update delete) functionalities on a persons data

A brief description on how the api can be used


## Testing


for the test file visit test.py


## UML REPRESENTATION

[![UML Diagram](https://github.com/marveldo/Crud-Functionality/blob/main/UML%20diagram%20for%20database.png)]

## 
#### Create Profile
```http
  GET /api
```

#### Method of Usage
```http
  data = {"name": "anyname"}
  requests.post(f'https://crud-functionality-hqud.onrender.com/api/{id}/',json = data)

```
#### What it returns
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

#### Method of Usage
```http
  data = {"name": "anyname"}
  requests.get(f'https://crud-functionality-hqud.onrender.com/api/{id}/')

``` 
#### What it returns
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

#### Method of Usage
```http
  data = {"name": "Updated name"}
  requests.put(f'https://crud-functionality-hqud.onrender.com/api/{id}/',json = data)

```
#### What it returns
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

#### Method of Usage
```http
  requests.delete(f'https://crud-functionality-hqud.onrender.com/api/{id}/')

```
#### What it returns
```http
  Succesfully deleted
```

## Deployment

Project was succesfully deployed to render with 
the live file being https://crud-functionality-hqud.onrender.com/api


