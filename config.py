from urllib.parse import urlparse

ENV = "deploy"

if ENV == 'dev':
    DATABASE_CONFIG = {
        'host': "localhost",
        'database': "postgres",
        'user': "simone",
        'password': "pic4ser",
        'port': "5432"

    }
else: 
    uri = "localhost"
    parsed_uri = urlparse(uri)

    DATABASE_CONFIG = {
        'host': "localhost",
        'database': "postgres",
        'user': "simone",
        'password': "pic4ser",
        'port': "5432"
    } 
