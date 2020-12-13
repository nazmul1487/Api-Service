# Api-Service

## Setup the Application
It is best to use the python `virtualenv` tool to build locally:

- **Clone the repository**

```sh
 $ git clone https://github.com/nazmul1487/Api-Service
 $ cd Api-Service
```

- **Setup Virtual environment** 
 ```sh
  $ virtualenv env
  $ source ./env/bin/activate
  ```  

## Run the Application
Migrations and migrate 
   ```sh
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```
Run server
  ```sh
  $ python manage.py runserver
  ```
visit http://127.0.0.1:8000 to view the application

## Url Pattern
Login 
 ```sh
  $ http://127.0.0.1:8000/login/
 ```
Logout
```sh
  $ http://127.0.0.1:8000/logout/
```
Data Form
```sh
  $ http://127.0.0.1:8000/
```

## Work Flow
For details please check the issues of the application.


