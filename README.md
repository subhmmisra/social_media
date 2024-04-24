Social Media API
==============================

Social Media Backend

## Getting up and running

Minimum requirements: Docker, **pip, python3, & [postgres][install-postgres]**, setup is tested on Mac OSX only.

```
clone repo
git clone https://github.com/subhmmisra/social_media.git
```

Install Virtual env

```
pip install virtualenv
```


Once you have created/activated virtual environment. Install all the python requirements

```
pip install -U -r requirements.txt
```

Create the database 

```
createdb social_db
```

O

Install pre-commit

```
pre-commit install
```

Update db and run inital migration

```
python manage.py migrate
```

Running the API

Build Docker Image

```
docker-compose build
```

Start the application

```
docker-compose up
```

If using linux/ubuntu follow: http://stackoverflow.com/a/34631976/1906584


API Endpoints:

Base URL: http://localhost:8000/api/v1/ (assuming default port mapping)


For API documentation plese run following commands

```
mkdocs serve
```
Once mkdocs is running, browse to http://127.0.0.1:8000/ 

## Contributing

Golden Rule:

> Anything in **master** is always **deployable**.

Avoid working on `master` branch, create a new branch with meaningful name, send pull request asap. Be vocal!

[install-postgres]: http://www.gotealeaf.com/blog/how-to-install-postgresql-on-a-mac
