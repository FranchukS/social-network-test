## Test task: Social Network
###  Description
This is a task to build a simple Social network API using Django Rest Framework.
Basic models:
*  User
*  Post (always made by a user)
*  Like

### Basic Features:
* user signup
* user login
* post creation
* post like/unlike
* analytics about how many likes was made. API return analytics
aggregated by day.
* user activity, an endpoint which will show when user was login last time and when he
made last request to the service.
Requirements:
* token authentication using JWT


### Installing using GitHub:

    git clone https://github.com/FranchukS/social-network-test.git

### install requirements
    - python -m venv venv\
    - venv\Scripts\activate (on Windows)\
    - source venv/bin/activate (on macOS or bash)\
    - pip install -r requirements.txt

### set your ENV variable

    set SECRET_KEY=<your secret key> (on Windows)\
    export SECRET_KEY=<your secret key> (on macOS)\

### run migrations and server
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

### create superuser for having admin status
    python manage.py createsuperuser

## Endpoints:
* ```api/user/signup/``` (POST) - register new user(create)
* ```api/user/login/``` (POST) - get JWT pair for authentication
* ```api/user/login/token-refresh/``` - refresh access token
* ```api/user/login/token-verify/``` - verify tokens
* ```api/user/me/``` - personal page of authenticated user where can update info
* ```api/user/activity/``` - (GET) show when users was login last time and when they
made last request to the service. Can use parameters for filter by user_id and username
(e.g. ?user_id=1,3 or ?username=admin)
* ```/api/post/``` (GET/POST) - list of posts / create new post
* ```/api/post/<int>/``` (GET/PUT/PATCH/DELETE) - detail page of post
(delete - only change is_active attribute on False)
* ```/api/post/<int>/like/``` (POST) - add Like to Post or made it not active (toggle)
* ```/api/analytics/``` (GET) - analytics about how many likes was made.
API return analytics aggregated by day. Example url /api/analytics/?date_from=2020-02-02&date_to=2020-02-15 
* ```/api/doc/swagger/``` - swagger API documentation
