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

If tools like Postman are used first of all acces and refresh tokes should be gathered from address
http://127.0.0.1:8000/api/token where email and password of previously created user should be passed
Also http://127.0.0.1:8000/api/token/refresh/ and http://127.0.0.1:8000/api/token/verify/ are allowed to
interact with

token expires each hour and refresh could be done during one day (24h)

Main endpoints to interact with api are:
http://127.0.0.1:8000/api/v1/user/ (allowed to everyone)
http://127.0.0.1:8000/api/v1/restaurant/ (allowed to view by staff and manage by restauranters)

http://127.0.0.1:8000/api/v1/menu/  (authorized users(staff) could view here menus which have been added 
                                        in todays date)

http://127.0.0.1:8000/api/v1/vote/  (allow authorized staff to create only one one for menu which they preffer
                                        you could delete your previous choice and made new one or wait 23 hours
                                        untill new vote will be allowed. Also this Api will provide your vote to
                                        be able gte familiar with it after creation. Restraunters are not allowed
                                            to perform opperations with votes)
http://127.0.0.1:8000/api/v1/daymenu/ (Endpoint which return menu of the day or if rating is equal list of menues)



Folder test include two python files with tests for authorization and restaurant creation 
to run them just provide in terminal command pytest -v or pytest -k test_function_name

(Note, i am not shure in tests every time get's an erro Uproperly configured Database do not know what to do with it
and due to lack of time just leave it as it where) Tests are my weak side :(

Have a nice day and good luck!




P.S. I just realized that I’ve totally forgotten about versions support. I barely know that version is included in the header of an API HTML response received from the server. Nonetheless, it was a part of the task and it misses,in any case, I will deal with it 
