from os import environ
from cassandra.cqlengine import connection
from cassandra.auth import PlainTextAuthProvider
from stream_framework import settings

auth_provider = PlainTextAuthProvider(
        username=environ['CASSANDRA_USERNAME'],
         password=environ['CASSANDRA_PASSWORD'])

def setup_connection():
    connection.setup(
        hosts=[environ['CASSANDRA_HOST']],
        consistency=settings.STREAM_CASSANDRA_CONSISTENCY_LEVEL,
        default_keyspace=settings.STREAM_DEFAULT_KEYSPACE,
        auth_provider=auth_provider,
        **settings.CASSANDRA_DRIVER_KWARGS
    )
