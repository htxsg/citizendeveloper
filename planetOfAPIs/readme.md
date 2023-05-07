# Planet of the APIs
Sharing about APIs by @pyx7b

# ChatGPT Prompts
The folllowing prompts was used during the presentation - results may vary :)

## GraphQL Prompts
1. Create a graphql schema for petstore
```
type Query {
  pets: [Pet!]!
  pet(id: ID!): Pet
}

type Mutation {
  addPet(input: AddPetInput!): Pet!
  updatePet(id: ID!, input: UpdatePetInput!): Pet!
  deletePet(id: ID!): ID!
}

input AddPetInput {
  name: String!
  species: String!
  breed: String
  age: Int
  owner: String
}

input UpdatePetInput {
  name: String
  species: String
  breed: String
  age: Int
  owner: String
}

type Pet {
  id: ID!
  name: String!
  species: String!
  breed: String
  age: Int
  owner: String
}
```

2. populate 10 example data for schema
```
{
  "data": {
    "pets": [
      {
        "id": "1",
        "name": "Max",
        "species": "Dog",
        "breed": "Labrador Retriever",
        "age": 5,
        "owner": "John Doe"
      },
      {
        "id": "2",
        "name": "Fluffy",
        "species": "Cat",
        "breed": "Persian",
        "age": 3,
        "owner": "Jane Smith"
      },
      {
        "id": "3",
        "name": "Buddy",
        "species": "Dog",
        "breed": "Golden Retriever",
        "age": 2,
        "owner": "John Doe"
      },
      {
        "id": "4",
        "name": "Garfield",
        "species": "Cat",
        "breed": null,
        "age": 6,
        "owner": "Amanda Lee"
      },
      {
        "id": "5",
        "name": "Rocky",
        "species": "Dog",
        "breed": "German Shepherd",
        "age": 4,
        "owner": "Mike Johnson"
      },
      {
        "id": "6",
        "name": "Mittens",
        "species": "Cat",
        "breed": "Siamese",
        "age": 1,
        "owner": "Jane Smith"
      },
      {
        "id": "7",
        "name": "Luna",
        "species": "Dog",
        "breed": "Siberian Husky",
        "age": 3,
        "owner": "Amanda Lee"
      },
      {
        "id": "8",
        "name": "Simba",
        "species": "Cat",
        "breed": "Bengal",
        "age": 2,
        "owner": "Mike Johnson"
      },
      {
        "id": "9",
        "name": "Bella",
        "species": "Dog",
        "breed": "Poodle",
        "age": 1,
        "owner": "John Doe"
      },
      {
        "id": "10",
        "name": "Whiskers",
        "species": "Cat",
        "breed": "Domestic Shorthair",
        "age": 4,
        "owner": "Jane Smith"
      }
    ],
    "pet": {
      "id": "1",
      "name": "Max",
      "species": "Dog",
      "breed": "Labrador Retriever",
      "age": 5,
      "owner": "John Doe"
    }
  }
}
```

3. what is the graphql query for cat that are younger than 3 years old
```
query {
  pets(species: "Cat", age_lt: 3) {
    id
    name
    age
    breed
  }
}
```
## JSON Prompts
1. Create a JSON schema for employees
```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "email": {
      "type": "string",
      "format": "email"
    },
    "phone": {
      "type": "string"
    },
    "address": {
      "type": "object",
      "properties": {
        "street": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "state": {
          "type": "string"
        },
        "zip": {
          "type": "string"
        }
      },
      "required": ["street", "city", "state", "zip"]
    },
    "department": {
      "type": "string"
    },
    "salary": {
      "type": "number"
    },
    "hireDate": {
      "type": "string",
      "format": "date-time"
    }
  },
  "required": ["id", "name", "email", "phone", "address", "department", "salary", "hireDate"]
}
```

2. Populate schema with 5 employees
```
{
  "employees": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "johndoe@example.com",
      "phone": "123-456-7890",
      "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip": "62704"
      },
      "department": "HR",
      "salary": 50000,
      "hireDate": "2020-01-01T09:00:00Z"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "janesmith@example.com",
      "phone": "987-654-3210",
      "address": {
        "street": "456 Oak Ave",
        "city": "Shelbyville",
        "state": "IL",
        "zip": "62701"
      },
      "department": "Finance",
      "salary": 60000,
      "hireDate": "2018-05-15T14:30:00Z"
    },
    {
      "id": 3,
      "name": "Mark Johnson",
      "email": "markjohnson@example.com",
      "phone": "555-123-4567",
      "address": {
        "street": "789 Pine St",
        "city": "Capital City",
        "state": "IL",
        "zip": "62703"
      },
      "department": "IT",
      "salary": 70000,
      "hireDate": "2017-09-10T11:45:00Z"
    },
    {
      "id": 4,
      "name": "Anna Lee",
      "email": "annalee@example.com",
      "phone": "444-789-0123",
      "address": {
        "street": "321 Elm Rd",
        "city": "Shelbyville",
        "state": "IL",
        "zip": "62701"
      },
      "department": "Marketing",
      "salary": 55000,
      "hireDate": "2019-03-20T08:15:00Z"
    },
    {
      "id": 5,
      "name": "Michael Brown",
      "email": "michaelbrown@example.com",
      "phone": "777-555-8888",
      "address": {
        "street": "567 Birch Ln",
        "city": "Capital City",
        "state": "IL",
        "zip": "62703"
      },
      "department": "Operations",
      "salary": 80000,
      "hireDate": "2016-11-01T13:00:00Z"
    }
  ]
}
```
## Curl Prompts
1. I want you to act as a Linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. Do not write explanations. Do not type commands unless I instruct you to do so. When I need to tell you something in English I will do so by putting text inside curly brackets {like this}. My first command is pwd.

2. curl -vI https://www.htx.gov.sg

3. curl https://petstore3.swagger.io/api/v3/pet/findByStatus?status=available

## NodeJS Prompts
1. Create an express API server that has 1 get method for retrieving pet by id and and 1 post method to add new pet

## FastAPI Prompts
1. Write an api server using fast API for a book store with book name, author and description.  5 books preloaded

2. Write a module that calls OpenAI API using requests to generate funning name for books


# Useful Links
- [Pet Store](https://petstore3.swagger.io)
- [JSON Cheatsheet](https://quickref.me/json.html)
- [Online JSON Editor](https://jsoneditoronline.org)
- [Code Beautify](https://codebeautify.org/jsonviewer)
- [Swagger Homne](https://app.swaggerhub.com/home)
- [Swagger Editor](https://editor-next.swagger.io/)
- [Curl Cheatsheet](https://quickref.me/curl)
- [Postman](https://www.postman.com)
- [OpenAI Playground](https://platform.openai.com/playground)

