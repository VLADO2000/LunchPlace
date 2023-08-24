Application luch place allow restaurants (their managers) to present themselves with
different menu every day, menu which will gather the highest grade will become the Menu of the day

Interaction with applications should be performed through API.

To launch server download git repo

Launch docker application, go in folder where app is stored and in terminal provide command 
$ docker-compose up -d --build

Container should start and database ready to connection will coopirate with web-server which could be acssed
by link http://127.0.0.1:8000/api/v1 or http://localhost:8000/api/v1

Applications could be used internaly in browser viw Django Rest Framework UI or with using such tools as Postman, 
Insomnia etc.

only view http://127.0.0.1:8000/api/v1/user/ will allow unauthorized users to perfrom actions, it had been made 
for brevity and convenience 
Here you will be able to register your first user with role staff(0) or restraunter(1)
Main endpoints to interact with api are:
http://127.0.0.1:8000/api/v1/user/ (allowed to everyone)
Json example to build(POST) a user via API:
 {
        "name": "Test",
        "password": "test",
        "email": "test@testua.com",
        "role": 0,
        "is_active": true
    }

If tools like Postman are used first of all acces and refresh tokes should be gathered from address
http://127.0.0.1:8000/api/token where email and password of previously created user should be passed
Example for token getiing toke, perform POST with body:
{
        
        "name": "Test",
        "password": "test",
        "email": "test@testua.com",
        "role": 0,
        "is_active": true
    }
and get a response like:
{
    "refresh": "tokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentoken",
    "access": "tokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentokentoken"
}

Also http://127.0.0.1:8000/api/token/refresh/ allow to regresh acces token:
{
        
       "refresh": "tokensImV4cCI6MTY5Mjk1ODQwNiwiaWF0IjoxNjkyODcyMDA2LCJqdGkiOiJjZTkyZtokentokenE3NWE3NTRhNTMxMzUxMyIsInVzZXJfaWQiOjJ9.IiO884PZOypu289P-unjMd3Wt0hfL9TWQC0AYWuVNHQ"
    }



and http://127.0.0.1:8000/api/token/verify/ are allowed to
interact with

token expires each hour and refresh could be done during one day (24h)

Than provide acces token in header with key Authorization and pass value in format JWT  tokentokentokentokentokentokenWNjZXNzIiwiZXhwIjoxNjkyNzg0MzQ3LCJpYXQiOjE2OTI3ODI4NDcsImp0aSI6Ijc3YWEwYWQyNjEzNDRhMWFiMWVkY2I0NzJjNDA4MDUwIiwidXNlcl9pZCI6M30.vSQeqbC8pT5Trt5xOgYMJEA9VzhPj4wMgrRCcDGCRUc

Then perform GET operation on any of links as authorized user

http://127.0.0.1:8000/api/v1/restaurant/ (allowed to view by staff and manage by restauranters)

http://127.0.0.1:8000/api/v1/menu/  (authorized users(staff) could view here menus which have been added 
                                        in todays date)

http://127.0.0.1:8000/api/v1/vote/  (allow authorized staff to create only one one for menu which they preffer
                                        you could delete your previous choice and made new one or wait 23 hours
                                        untill new vote will be allowed. Also this Api will provide your vote to
                                        be able gte familiar with it after creation. Restraunters are not allowed
                                            to perform opperations with votes)
http://127.0.0.1:8000/api/v1/daymenu/ (Endpoint which return menu of the day or if rating is equal list of menues)

In all case as database is empty you will recieve an empty list as a response. Let's try role of a restraunter at first, create soem restaurant and menu to it and than vote as user.
For this we need to create new user, do as written below just relase role to 1 which mean role = "restauranter"
{
    "name": "Restauranter",
    "password": "rest",
    "email": "rest@rest.com",
    "role": 1,
    "is_active": true
}

and with this body perfrom token authorization same as with user-staff. You could just shrink body to
{
    
    "password": "rest",
    "email": "rest@rest.com"
   
}

Now when we have token in our header let's create a restaurant by endpoint http://127.0.0.1:8000/api/v1/restaurant/ with body:
{
    "name": "PoseAtive",
    
}


and we will get as pesponse our result:
{
    "id": 2,
    "name": "PoseAtive",
    "created_at": "2023-08-24T10:39:15.192160Z",
    "updated_at": "2023-08-24T10:39:15.192181Z",
    "users_emails": [
        "rest@rest.com"
    ]
}

You are able to create restaurants without passing and email to it, but if you want to create with several managers feel free to pass several emails


It's predictable than we should create our menu by endpoint http://127.0.0.1:8000/api/v1/menu/
provide in POST body like:
{
    "name": "PoseAtiveMenuDay1",
    "food_items": "Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu",
    "rest_id": 2
}
And got a response:
{
    "id": 1,
    "name": "PoseAtiveMenuDay1",
    "food_items": "Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu",
    "vote_count": 0,
    "rest_repr": {
        "name": "PoseAtive"
    },
    "rest_id": 2,
    "created_at": "2023-08-24T10:45:01.316237Z",
    "updated_at": "2023-08-24T10:45:01.316260Z"
}

Greate, now we have our menu, as we are manager we can not vote, try it out http://127.0.0.1:8000/api/v1/vote/

{
    "detail": "Restauranter users are not allowed to create votes."
}
Same as users-staff can not maange menues and restaurants 


Than create several menues and choose one to vote as staff to chech daymenu, let,s do it...





Login as staff and provide same POST to end point http://127.0.0.1:8000/api/v1/vote/ with body:
{
    "menu_id": 1
    
}
And got the result:
{
    "id": 1,
    "menu": {
        "name": "PoseAtiveMenuDay1"
    },
    "menu_id": 1,
    "created_at": "2023-08-24T10:52:26.484605Z"
}
Vote is automaticaly assigned to you and you can view this  menu now and see that vote_count has increased by 1
[
    {
        "id": 1,
        "name": "PoseAtiveMenuDay1",
        "food_items": "Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu",
        "vote_count": 1,
        "rest_repr": {
            "name": "PoseAtive"
        },
        "rest_id": 2,
        "created_at": "2023-08-24T10:45:01.316237Z",
        "updated_at": "2023-08-24T10:52:26.480642Z"
    }
]
Than Try to vote again and response will be got:

{
    "detail": "You can't create a new vote until your existing votes have ended."
}
Let's Delete our Vote and see what happen to menu:
Just choose DELETE option to endpoint http://127.0.0.1:8000/api/v1/vote/1/ where 1 is id of our vote
and let's look again to our menu:
[
    {
        "id": 1,
        "name": "PoseAtiveMenuDay1",
        "food_items": "Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu",
        "vote_count": 0,
        "rest_repr": {
            "name": "PoseAtive"
        },
        "rest_id": 2,
        "created_at": "2023-08-24T10:45:01.316237Z",
        "updated_at": "2023-08-24T10:57:49.506749Z"
    }
]
no votes so far, but we need one to check our last endpoint http://127.0.0.1:8000/api/v1/daymenu/,
let's get it without any votes, what will we see?
as we have 2 menues with 0 votes both of them were returned:
[
    {
        "id": 1,
        "name": "PoseAtiveMenuDay1",
        "food_items": "Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu",
        "vote_count": 0,
        "rest_repr": {
            "name": "PoseAtive"
        },
        "rest_id": 2,
        "created_at": "2023-08-24T10:45:01.316237Z",
        "updated_at": "2023-08-24T10:57:49.506749Z"
    },
    {
        "id": 2,
        "name": "Nu-nu-dinner",
        "food_items": "Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu",
        "vote_count": 0,
        "rest_repr": {
            "name": "Nu-nu"
        },
        "rest_id": 3,
        "created_at": "2023-08-24T11:05:08.448696Z",
        "updated_at": "2023-08-24T11:05:08.448719Z"
    }
]

Let's bote for one of them and check than, i have chosen second one and now got as response:
[
    {
        "id": 2,
        "name": "Nu-nu-dinner",
        "food_items": "Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu--Menu",
        "vote_count": 1, #my vote is here
        "rest_repr": {
            "name": "Nu-nu"
        },
        "rest_id": 3,
        "created_at": "2023-08-24T11:05:08.448696Z",
        "updated_at": "2023-08-24T11:07:30.848028Z"
    }
]

Maybe we can can just put a day menu as restauranter with role 1 and that's will be, let's checkout and provide POST for endpointhttp://127.0.0.1:8000/api/v1/daymenu/

and i got this:
{
    "detail": "Method \"POST\" not allowed."
}
as well as DELETE not allowed. 


That's all for an API, i know it was late bate i recognized that instruction mentioned in test task mean instruction how to use 
endpoints nit just describe them, code remains the same i just can not leave you to explore all this body strutures and returned to clearly provide them


Folder test include two python files with tests for authorization and restaurant creation 
to run them just provide in terminal command pytest -v or pytest -k test_function_name

(Note, i am not shure in tests every time get's an erro Uproperly configured Database do not know what to do with it
and due to lack of time just leave it as it where) Tests are my weak side :(

Have a nice day and good luck!




P.S. I just realized that I’ve totally forgotten about versions support. I barely know that version is included in the header of an API HTML response received from the server. Nonetheless, it was a part of the task and it misses,in any case, I will deal with it 
