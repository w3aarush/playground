import chromadb as cdb
from chromadb.config import Settings

# client = cdb.Client(
#     Settings(
#         chroma_server_host='localhost',
#         chroma_server_http_port=8000
#     )
# )
# client = cdb.HttpClient(host='localhost',port=8000)

client = cdb.PersistentClient(path='./server_data')

storage_1 = client.get_or_create_collection(name='storage_1')
storage_2 = client.get_or_create_collection(name='storage_2')

storage_1.upsert(
    documents=[
        'My name is Aarush Singh.',
        'I live in localhost, 127.0.0.1',
        'I am enrolled in MCA.'
    ],
    ids=['1','2','3']
)

storage_2.upsert(
    documents = [
        'My name is user_2017.',
        "I live in localhost, 127.0.0.1",
        "I am studying in 8th standard."
    ],
    ids=['1','2','3'],
    metadatas = [
        {'name':'localhost'},
        {'location':'locahost district'},
        {'education':"HFINTLSCHL"}
    ]
)

print(client.list_collections())