
# An Api capable of CRUD(create read update delete) functionalities on a persons data 

## Table of Contents

- [API Documentation](#api-documentation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the API](#running-the-api)
  - [API Endpoints](#api-endpoints)
    - [Create a Person](#create-a-person)
    - [Get a Person by ID](#get-a-person-by-id)
    - [Update a Person](#update-a-person)
    - [Delete a Person](#delete-a-person)
  - [Request and Response Formats](#request-and-response-formats)
  - [Sample Usage](#sample-usage)
    - [Create a Person](#create-a-person-1)
    - [Get a Person by ID](#get-a-person-by-id-1)
    - [Update a Person](#update-a-person-1)
    - [Delete a Person](#delete-a-person-1)

  - [Testing](#testing)
  - [Deployment](#deployment)
  - [challenges and limitations](#challenges-and-limitation)
 


## Introduction

The Profile API is programmed to perform CRUD operations on a "profiles" resource. It provides endpoints for creating, fetching, updating, and deleting profiles records in a Postgres database. The API is built using Django and postgres, making it easy to use and extend.

This readme file contains explanations on how to use the file and also contains documentation on the file

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- python must be installed on your system
- must have install django on your system
- django rest framework must have been installed
- corshearders must be installed



### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-own-username/Crud-Functionality.git
   ```

2. Navigate to the project directory:

   ```bash
      cd Crud-Functionality
   ```

3. Install the project dependencies:

   ```bash
      pip install -r requirements.txt 
   ```

### Running the API

1. Start the Postgres server if not already running.



2. Start the API by running:

   ```bash
     python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Create a Person

- **URL:** `/api`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "name": "Michael Oliver",
  }
  ```

- **Response:**

  ```json
  {
    "_id": "1",
    "name": "Michael Oliver",
    
  }
  ```

### Get a Person by ID

- **URL:** `/api/1/`
- **Method:** `GET`
- **Response:**

  ```json
  {
    "_id": "1",
    "name": "Michael Oliver",
    
  }
  ```

### Update a Person

- **URL:** `/api/1/`
- **Method:** `PUT`
- **Request Body:**

  ```json
  {
    "name": " Updated Michael Oliver",
  }
  ```

- **Response:**

  ```json
  {
    "_id": "1",
    "name": "Updated Michael Oliver",
   
  }
  ```

### Delete a Person

- **URL:** `/api/id/`
- **Method:** `DELETE`
- **Response:** `204 No Content`

## Request and Response Formats

- **Request Format:** Requests should be sent in JSON format.
- **Response Format:** Responses are in JSON format.

## Sample Usage

Here are some sample requests and responses for the Person API:

### Create a Person

**Request:**

```http
POST /api/persons
Content-Type: application/json

{
  "name": "Michael john",
  
}
```

**Response:**

```json
{
  "_id": "1",
  "name": "Michael John",  
  
}
```

### Get a Person by ID

**Request:**

```http
GET /api/1/
```

**Response:**

```json
{
  "_id": "5fd5a4f1b2f317001c5c7c65",
  "name": "Michael John",
  
}
```

### Update a Person

**Request:**

```http
PUT /api/1/
Content-Type: application/json

{
  "name": "Updated Michael",
}
```

**Response:**

```json
{
  "_id": "1",
  "name": "Updated Michael",
}
```

### Delete a Person

**Request:**

```http
DELETE /api/1/
```

**Response:**

```http
 status:204 No Content
```

## Testing
for the test script visit https://github.com/marveldo/Crud-Functionality/blob/main/test.py

a picture of the response when testing the api 

![Picture](https://github.com/marveldo/Crud-Functionality/blob/main/Hng%20test.png)



for Validation used in the development of the api visit https://github.com/marveldo/Crud-Functionality/blob/main/api/views.py


## Deployment

Project was succesfully deployed to render with 

the live file being https://crud-functionality-hqud.onrender.com/api

firstly i commited the project to github then went over to render to host directly from github 

it required downloading the requirements.txt file with pip install -r requirements.txt and then gunicorn was needed for the execution of the file 

## Challenges and limitation


Authentication methods not used


The data cannot be queried from the name more from the id


