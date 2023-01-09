# Address Book Application
Basic Flask and MongoDB test case application

## Running
Clone the repo and go to the directory:

```bash
$ git clone https://github.com/AlogluMustafaCan/Address_Book_Application.git
$ cd Address_Book_Application
```

Install the dependencies:

```bash
$ make init
```

Run the projec

```bash
$ make run
```

The service will be reachable on ```http://localhost:8080```

## Usage

### Endpoint

POST http://localhost:8080

REQUEST:

```json
{
    "name": "Test",
    "address": "Test",
    "phone": "Test",
    "mobile_phone": "Test",
    "email": "Test@Test.com"
}
```

RESPONSE:

```json
{
    "address": "Test",
    "email": "Test@Test.com",
    "mobile_phone": "Test",
    "name": "Test",
    "phone": "Test"
}
```

GET http://localhost:8080/get/Test

RESPONSE

```json
{
    "address": "Test",
    "email": "Test",
    "mobile_phone": "Test",
    "name": "Test",
    "phone": "Test"
}
```

PUT http://localhost:8080/update/Test

REQUEST

```json
{
    "name": "TestUpdate",
    "address": "TestUpdate",
    "phone": "TestUpdate",
    "mobile_phone": "Test",
    "email": "Test@Test.com"
}
```

RESPONSE

```json

```

DELETE http://localhost:8080/delete/Test

```json

```

