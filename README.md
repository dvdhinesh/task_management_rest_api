#### Task Management with RESTful API using JWT

### Terminal commands

Environment Setup:
```sh
$ python3 -m venv /source/path/folder/destination
$ . /source/path/folder/destination/bin/activate
$ pip install -r requirements.txt
```

To run test:
```sh
$ export TASK_MANAGEMENT_REST_ENV=test
$ python3 manage.py test
```

To run application in development mode:
```sh
$ export TASK_MANAGEMENT_REST_ENV=dev
$ python3 manage.py db init
$ python3 manage.py db migrate --message 'initial database migration'
$ python3 manage.py db upgrade
$ python3 manage.py run
```

To run application in production mode:
```sh
$ export TASK_MANAGEMENT_REST_ENV=prod
$ python3 manage.py db upgrade
$ python3 manage.py run
```


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"


### Workflow ####

    * Register the API consumers as users
    * Login to the system and obtain Authorization token
    * Create/Update/Fetch/Delete the tasks
    * Logout from the system


### Assumptions ####

    * Used Flask and its extensions to build this API system compatible with Swagger UI
    * Used SQLAlchemy as the ORM and APScheduler for cron functions
    * Crons are enabled in both development and production environment
    * Each cron will run twice in development environment due to reloader (https://stackoverflow.com/questions/25504149/why-does-running-the-flask-dev-server-run-itself-twice)
    * Task expiry cron should trigger most advanced function like email or slack notification. To keep things simple i used logging through print statement
    * All datetimes are assumed to be in UTC
    * All are authenticated endpoints except user registration
    * Once the token was blacklisted by means of logout, that token cannot be reused again.


### Improvements ####

    * Send emails/slack notifications on task expiry to related users


### Endpoints ####

User Endpoints:
```sh
POST: http://127.0.0.1:5000/user/
SAMPLE: curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"password": "domain.com", "email": "dhinesh@domain.com"}' 'http://127.0.0.1:5000/user/'
```

Authentication Endpoints:
```sh
POST: http://127.0.0.1:5000/auth/login
SAMPLE: curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"password": "domain.com", "email": "dhinesh@domain.com"}' 'http://127.0.0.1:5000/auth/login'
```

```sh
POST: http://127.0.0.1:5000/auth/logout
SAMPLE: curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'Authorization: token_generated_during_login' 'http://127.0.0.1:5000/auth/logout'
```

Task Endpoints:
```sh
POST: http://127.0.0.1:5000/task/
SAMPLE: curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'Authorization: token_generated_during_login' -d '{"expires_on": "2019-08-19T03:32:12.383Z", "name": "Enter your task name here", "description": "Enter your description name here"}' 'http://127.0.0.1:5000/task/'
```

```sh
GET: http://127.0.0.1:5000/task/
SAMPLE: curl -X GET --header 'Accept: application/json' --header 'Authorization: token_generated_during_login' 'http://127.0.0.1:5000/task/'
```

```sh
GET: http://127.0.0.1:5000/task/{public_task_id}
SAMPLE: curl -X GET --header 'Accept: application/json' --header 'Authorization: token_generated_during_login' 'http://127.0.0.1:5000/task/public_task_id'
```

```sh
PATCH: http://127.0.0.1:5000/task/{public_task_id}
SAMPLE: curl -X PATCH --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'Authorization: token_generated_during_login' -d '{"expires_on": "2019-08-19T03:32:12.398Z", "name": "Enter your modified task name here", "description": "Enter your modified description name here"}' 'http://127.0.0.1:5000/task/public_task_id'
```

```sh
DELETE: http://127.0.0.1:5000/task/{public_task_id}
SAMPLE: curl -X DELETE --header 'Accept: application/json' --header 'Authorization: token_generated_during_login' 'http://127.0.0.1:5000/task/public_task_id'

```
