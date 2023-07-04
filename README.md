# Zebrands backend test

## This project was made using WSL and the next techs:
    Django
    Django-restframework

# The project:

This is REST project than was made with Django-rest framework

Project features:

- The routes are protected by user authentication and by a jsonJWT, to query almost all routes it is necessary to send the token in the headers.

- The app has automatic documentation

- There are 2 types of users, anonymous and administrators, the administrator user can do CRUD of products and users.

- The anonymous user can only view the information, can search all products or by id but cannot modify the records, and there is a counter to determine how many times the anonymous user searched a product by id.

- An email is sent when a product is edited or deleted.

- .gitignore has been added using the template of https://gitignore.io/


# Routes:

URL_BASE = http://127.0.0.1:8000/

## For Token

/token/              
/token/refresh/         
                          
## For Productos   

/products/api/v1/       
/products/api/v1/<uuid>  

## For Users

/users/api/v1/                 
/users/api/v1/<id_number>  
