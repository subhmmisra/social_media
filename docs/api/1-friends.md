#Social Media API

##Register User
```
POST /api/v1/auth/register
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Content-Type**  | application/json


__Request__
```json
{
    "first_name": "User 5",
    "last_name": "Mishra",
    "email": "user5@alpha.com",
    "password": "123"
}
```

__Response__
```json
Status: 201 Created
{
    "id": "63eb4ea7-e0f9-4625-b573-6f36c28a2094",
    "first_name": "User 5",
    "last_name": "Mishra",
    "email": "user5@alpha.com",
    "phone_number": null,
    "full_name": "",
    "tokens": {
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzOTUyMzExLCJpYXQiOjE3MTM5NDg3MTEsImp0aSI6IjQ3NmZlNmFiZjQ3NDRjOTRiNmZlZjUxNzQyMjEyZmI0IiwidXNlcl9pZCI6IjU0NDhkODM2LWVlMTYtNDk2MS1hZTE0LTZiN2Y0NzJiODFkMyJ9.gXzt-C_5xAnYmPwqL1WJjqp3jS4RNFujEtaItm23EiA",
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNTI0NDcxMSwiaWF0IjoxNzEzOTQ4NzExLCJqdGkiOiI4OGQ0ZmNlMTk0MGI0ZjJlOGE2ZmIyYzIzNGI0Y2U1NyIsInVzZXJfaWQiOiI1NDQ4ZDgzNi1lZTE2LTQ5NjEtYWUxNC02YjdmNDcyYjgxZDMifQ.JPE1CXXih_HR8NHZMEKdJCxgH9P8jR66Y3R527qnbDY"
    }
}
```

##Login User
```
POST /api/v1/auth/login
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Content-Type**  | application/json

__Request__
```json
{
    "email": "subhmmisra03091@gmail.com",
    "password": "123"
}
```

__Response__
```json
Status: 200 - Ok
{
    "first_name": "Albert",
    "last_name": "Kumar",
    "email": "subhmmisra03091@gmail.com",
    "phone_number": null,
    "full_name": "",
    "tokens": {
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzOTUzOTc3LCJpYXQiOjE3MTM5NTAzNzcsImp0aSI6IjY2ODUxZTc0Mzk0MjQ1ZmNhNTgzNWYzZjE5YmY0Y2ViIiwidXNlcl9pZCI6ImE1YWY5MWU4LWM3MmUtNGQ5My1hMjgwLWI5NmEwY2I2NDA4MCJ9.I56iBiuJqtrsqKEpoU3dxQZN4lUnRnuhRJ3vlsz9vuA",
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNTI0NjM3NywiaWF0IjoxNzEzOTUwMzc3LCJqdGkiOiJhYTAzMTAzMDQ3NGM0OTg3YjMyOWZiZmI0ZmUyYThkOSIsInVzZXJfaWQiOiJhNWFmOTFlOC1jNzJlLTRkOTMtYTI4MC1iOTZhMGNiNjQwODAifQ.Gqcz0Js6tXv20MDL3OeK7uZlwUD8F_o98be3rHXFau8"
    }
}
```

##List Users
```
GET /api/v1/users
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Authorization** | Bearer {{TOKEN}}
**Content-Type**  | application/json


__Response__
```json
Status: 200 - Ok
```json
{
    "count": 12,
    "next": "http://127.0.0.1:8000/api/v1/users?page=2",
    "previous": null,
    "results": [
        {
            "first_name": "User 9",
            "last_name": "--",
            "email": "user9@alpha.com",
            "phone_number": null,
            "full_name": ""
        },
        {
            "first_name": "User 8",
            "last_name": "--",
            "email": "user8@alpha.com",
            "phone_number": null,
            "full_name": ""
        },
        {
            "first_name": "User 7",
            "last_name": "--",
            "email": "user7@alpha.com",
            "phone_number": null,
            "full_name": ""
        },
        {
            "first_name": "User 6",
            "last_name": "--",
            "email": "user6@alpha.com",
            "phone_number": null,
            "full_name": ""
        },
        {
            "first_name": "User 5",
            "last_name": "--",
            "email": "user5@alpha.com",
            "phone_number": null,
            "full_name": ""
        },
        {
            "first_name": "User 4",
            "last_name": "--",
            "email": "user4@gmail.com",
            "phone_number": null,
            "full_name": ""
        },
        {
            "first_name": "User 3",
            "last_name": "--",
            "email": "user3@gmail.com",
            "phone_number": null,
            "full_name": ""
        },
        {
            "first_name": "User 2",
            "last_name": "--",
            "email": "user2@gmail.com",
            "phone_number": null,
            "full_name": ""
        },
        {
            "first_name": "User 1",
            "last_name": "--",
            "email": "user1@gmail.com",
            "phone_number": null,
            "full_name": ""
        },
        {
            "first_name": "Shubham",
            "last_name": "Mishra",
            "email": "subhmmisra@gmail.com",
            "phone_number": null,
            "full_name": ""
        }
    ]
}
```

##List Users
```
GET /api/v1/users?search=shubh
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Authorization** | Bearer {{TOKEN}}
**Content-Type**  | application/json


__Response__
```json
Note: It works with first_name/last_name and email as well
```

```json
Status: 200 - Ok
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "first_name": "Shubham",
            "last_name": "Mishra",
            "email": "subhmmisra@gmail.com",
            "phone_number": null,
            "full_name": ""
        }
    ]
}
```

## Send Friend Request

```
POST /api/v1/friendship/send_requests
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Authorization** | Bearer {{TOKEN}}
**Content-Type**  | application/json


__Request__
```json
{
    "sent_to": "0ab51ffa-648d-4146-91ff-d99dc81a9444" 
}
```

__Response__
```json
Status: 200 - Ok
{
    "id": "7e103cfb-d855-4a2a-aff9-d041b9a77d1b",
    "status": 1,
    "sent_to": {
        "first_name": "User 5",
        "last_name": "--",
        "email": "user5@alpha.com",
        "phone_number": null,
        "full_name": ""
    },
    "sent_from": {
        "first_name": "Albert",
        "last_name": "Kumar",
        "email": "subhmmisra03091@gmail.com",
        "phone_number": null,
        "full_name": ""
    }
}
```


## List Pending Friend Requests

```
GET /api/v1/friendship/list_request
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Authorization** | Bearer {{TOKEN}}
**Content-Type**  | application/json


__Response__
```json
Note: It lists all the pending friend requests
```
```json
Status: 200 - Ok
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "f283493a-eb6d-40b5-9c44-8392e08d6b39",
            "status": 1,
            "sent_to": {
                "first_name": "Albert",
                "last_name": "Kumar",
                "email": "subhmmisra03091@gmail.com",
                "phone_number": null,
                "full_name": ""
            },
            "sent_from": {
                "first_name": "User 2",
                "last_name": "--",
                "email": "user2@gmail.com",
                "phone_number": null,
                "full_name": ""
            }
        }
    ]
}
```

## List Accepted Friend Requests (i.e. Friends)

```
POST /api/v1/friendship/list_request?request_type=accepted
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Authorization** | Bearer {{TOKEN}}
**Content-Type**  | application/json


__Response__
```json
Note: it lists down all the accepted friend request
```

```json
Status: 200 - Ok
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "9aecd3c3-4817-4e68-ac39-2493e2cd10db",
            "status": 2,
            "sent_to": {
                "first_name": "Albert",
                "last_name": "Kumar",
                "email": "subhmmisra03091@gmail.com",
                "phone_number": null,
                "full_name": ""
            },
            "sent_from": {
                "first_name": "User 3",
                "last_name": "--",
                "email": "user3@gmail.com",
                "phone_number": null,
                "full_name": ""
            }
        }
    ]
}
```

## Accept Friend Request

```
POST /api/v1/friendship/0d28e551-3c15-49d8-84f5-60e8215cae2c/request_action
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Authorization** | Bearer {{TOKEN}}
**Content-Type**  | application/json


__Request__
```json
{
    "action": "accept"
}
```

__Response__
```json
Status: 200 - Ok
"friend-request action successful"
```

## Reject Friend Request

```
POST /api/v1/friendship/0d28e551-3c15-49d8-84f5-60e8215cae2c/request_action
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Authorization** | Bearer {{TOKEN}}
**Content-Type**  | application/json


__Request__
```json
{
    "action": "decline"
}
```

__Response__
```json
Status: 200 - Ok
"friend-request action successful"
```