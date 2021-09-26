# Backend API for [Daemon's libs](https://github.com/suwalszczyzna/libs-react) app
Side project

Based on [Django](https://www.djangoproject.com/) and [django-rest-framework](https://www.django-rest-framework.org/)

# Features
* Rest API: for models
* Service API: parses and returning site meta info and favicons from given URL
* Pagination and filtering
* Models with NanoID

# Working demo
API is deployed on heroku. You can play with it using postman or [frontend app](https://daemon-libs.netlify.app/)

Heroku url: `https://libs-django.herokuapp.com/api/`

# Endpoints
## Standard endpoints:
Here is the API docs: https://libs-django.herokuapp.com/api/
* `link/` - GET and POST link items
* `tags/` - GET and POST tags items

## Custom endpoints:
#### `service/site_info/` - returns site info of your url

- example: `service/site_info/?url=https://www.awwwards.com/`
    
    ```json
    {
        "title": "Awwwards - Website Awards - Best Web Design Trends",
        "description": "Awwwards are the Website Awards that recognize and promote the talent and effort of the best developers, designers and web agencies in the world.",
        "base_url": "www.awwwards.com"
    }
    ```
  

#### `service/site_favicon/` - returns favicon of your url
- example: `service/site_favicon/?url=https://www.awwwards.com/`
    ```json
    {
        "icon": "https://assets.awwwards.com/assets/images/favicon.svg"
    }
    ```


# Quick install
1. Clone repo
2. Install dependencies: `pip install -r requirements.txt`
3. App needs PostgreSQL DB so you have to install and run it by your own
4. Export necessary env variables:
    ```
   POSTGRES_HOST
   POSTGRES_NAME
   POSTGRES_PASSWORD
   POSTGRES_PORT
   POSTGRES_USER
   SECRET_KEY
   ```
5. Make migrations: `python manage.py makemigrations`
6. Run the app: `python manage.py runserver`