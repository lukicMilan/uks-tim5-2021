# GitHub Application

## Team

Milana Tucakov
Nikola Zejak
Milan Lukic

## Requirements

[Django]>=3.0,<4.0(https://docs.djangoproject.com/en/4.0/)
psycopg2>=2.8
[Docker](https://www.docker.com/get-started)

## Set environment variables

Rename the `dotenv` file to the `.env`. And fill your values

```shell
SECRET_KEY=your_secret_key
POSTGRES_NAME=your_postgres_name
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
```

## To run manage.py commands:

```
docker-compose run django $COMMAND
```

## To run docker image:

```
docker-compose up
```
