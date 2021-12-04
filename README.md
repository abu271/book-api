# Django Book API
![Django Book API](https://github.com/abuDarda97/book-api/workflows/Python%20application/badge.svg)

Simple API using Django for creating books and authors

## **Requirements**
- Docker [version `19.03.13`]
- Docker Compose [version `1.27.4`]

## **Installation**
1. Clone the repo
2. Run `docker-compose build`
3. Next run `docker-compose up`
4. Access API on `http://localhost:8000/`

# **API Endpoints**
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

## **Books**

## View

Endpoint |HTTP Method 
-- | -- |
`/api/book/books/:id` | GET

## List 
Endpoint |HTTP Method 
-- | -- |
`/api/book/books/{params}` | GET

Optional params to filter the list of books
Param |Type | Description 
-- | -- | --|
name | string | the title name of the book
publication_year | number | year the book was published 
edition | number | the book edition
authors | string | author's name

## Create

Endpoint |HTTP Method 
-- | -- |
`/api/book/books` | POST

Fields |Type | Description 
-- | -- | --|
name | string | the title name of the book
publication_year | number | year the book was published 
edition | number | the book edition
authors | number | the author's id

## Edit

Endpoint |HTTP Method 
-- | -- |
`/api/book/books/:id` | PUT

Updatable field |Type 
-- | -- |
name | string
publication_year | number
edition | number
authors | number

## **Authors**

## Create 

Endpoint |HTTP Method 
-- | -- |
`/api/author/authors` | POST

Fields |Type | Description 
-- | -- | --|
name | string | the full name of the author

## View

Endpoint |HTTP Method 
-- | -- |
`/api/author/authors/:id` | GET

## List
Endpoint |HTTP Method 
-- | -- |
`/api/author/authors` | GET