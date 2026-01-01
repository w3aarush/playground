import chromadb as db
from chromadb.config import Settings

admin_client = db.AdminClient(Settings(is_persistent=True,persist_directory='./localserver'))

admin_client.create_tenant(name='aarush')   # creating tenants
admin_client.create_database(name='db_01', tenant='aarush')    # creating database
admin_client.create_database(name='db_02', tenant='aarush')    # creating database

admin_client.create_tenant(name='rahul')    # creating tenants
admin_client.create_database(name='db_01', tenant='rahul')     # creating database
admin_client.create_database(name='db_02', tenant='rahul')     # creating database

# connecting to the databse using HttpClient
aarush_client = db.HttpClient(host='127.0.0.1',port=8000,tenant='aarush',database='db_01')
# creating collection for aarush in db_01
collection_1 = aarush_client.get_or_create_collection(name='collection_01')
collection_2 = aarush_client.get_or_create_collection(name='collection_02')

# adding data in collections
collection_1.upsert(ids=['1','2','3'],
                    documents=[
                        'My name is Aarush Singh.',
                        'I live in localhost',
                        'I am enrolled in MCA'
                    ])

collection_2.upsert(ids=['1','2','3'],
                    documents=[
                        'I am studying vector database.',
                        'I like data science.'
                    ])


aarush_client = db.HttpClient(    # client for aarush for db_02
    host='locahost',
    port=8000,
    tenant='aarush',
    database='db_02'
)

# creating collection for aarush in db_02
collection_1 = aarush_client.get_or_create_collection(name='collection_01')
collection_2 = aarush_client.get_or_create_collection(name='collection_02')

# adding data in collections
collection_1.upsert(ids=['1','2','3'],
                    documents=[
                        'My name is Aarush Singh.',
                        'I live in localhost',
                        'I am enrolled in MCA'
                    ])

collection_2.upsert(ids=['1','2','3'],
                    documents=[
                        'I am studying vector database.',
                        'I like data science.'
                    ])

############################################################################

# same procedures for client_rahul
# connecting to the databse using HttpClient

rahul_client = db.HttpClient(    # client for rahul for db_01
    host='locahost',
    port=8000,
    tenant='rahul',
    database='db_01'
)
# creating collection for rahul in db_01
collection_1 = rahul_client.get_or_create_collection(name='collection_01')
collection_2 = rahul_client.get_or_create_collection(name='collection_02')

# adding data in collections
collection_1.upsert(ids=['1','2','3'],
                    documents=[
                        'My name is Rahul Kumar.',
                        'I live in localhost',
                        'I am enrolled in MCA'
                    ])

collection_2.upsert(ids=['1','2','3'],
                    documents=[
                        'I am studying vector database.',
                        'I like data science.'
                    ])


rahul_client = db.HttpClient(    # client for rahul for db_02
    host='locahost',
    port=8000,
    tenant='rahul',
    database='db_02'
)

# creating collection for rahul in db_02
collection_1 = rahul_client.get_or_create_collection(name='collection_01')
collection_2 = rahul_client.get_or_create_collection(name='collection_02')

# adding data in collections
collection_1.upsert(ids=['1','2','3'],
                    documents=[
                        'My name is Aarush Singh.',
                        'I live in localhost',
                        'I am enrolled in MCA'
                    ])

collection_2.upsert(ids=['1','2','3'],
                    documents=[
                        'I am studying vector database.',
                        'I like data science.'
                    ])