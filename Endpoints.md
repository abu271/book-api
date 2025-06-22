# **API Endpoints**
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

## **Authentication**

### Obtain Token

Endpoint | HTTP Method 
-- | -- |
`/api/v1/authtoken/` | POST

Fields | Type | Description 
-- | -- | --|
username | string | user's username
password | string | user's password

**Returns:**  
- 200 OK with `{ "token": "<token_value>" }` on success  
- 400/401 on error

---

## **Books**

### View

Endpoint | HTTP Method 
-- | -- |
`/api/v1/books/:id` | GET

### List 
Endpoint | HTTP Method 
-- | -- |
`/api/v1/books` | GET

Optional params to filter the list of books  
Param | Type | Description 
-- | -- | --|
name | string | the title name of the book
publication_year | number | year the book was published 
edition | number | the book edition
authors | string | author's name

### Create

Endpoint | HTTP Method 
-- | -- |
`/api/v1/books` | POST

Fields | Type | Description 
-- | -- | --|
name | string | the title name of the book
publication_year | number | year the book was published 
edition | number | the book edition
authors | number | the author's id

### Edit

Endpoint | HTTP Method 
-- | -- |
`/api/v1/books/:id` | PUT

Updatable field | Type 
-- | -- |
name | string
publication_year | number
edition | number
authors | number

---

## **Authors**

### Create 

Endpoint | HTTP Method 
-- | -- |
`/api/v1/authors` | POST

Fields | Type | Description 
-- | -- | --|
name | string | the full name of the author

### View

Endpoint | HTTP Method 
-- | -- |
`/api/v1/authors/:id` | GET

### List
Endpoint | HTTP Method 
-- | -- |
`/api/v1/authors` | GET

---

## **Users**

### Create

Endpoint | HTTP Method 
-- | -- |
`/api/v1/users` | POST

Fields | Type | Description 
-- | -- | --|
username | string | unique username
first_name | string | user's first name
last_name | string | user's last name
email | string | unique email address
password | string | password (min 8 chars)
date_of_birth | string | date of birth (DD-MM-YYYY)
gender | string | gender
ethnicity | string | (optional) ethnicity
religion | string | (optional) religion

### View

Endpoint | HTTP Method 
-- | -- |
`/api/v1/users/:id` | GET

### List

Endpoint | HTTP Method 
-- | -- |
`/api/v1/users` | GET