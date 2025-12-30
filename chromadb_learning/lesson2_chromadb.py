import chromadb as db
client = db.Client()

collection = client.get_or_create_collection(name='vector_db') # creates a new one if doesn't exist, otherwise fetches the existing one

collection.add( # for adding elements to collection
    documents= [
        'My name is Aarush Singh.',
        "I am learning managing vector databases."
    ],
    ids = ['id1','id2']
)

print('=='*50)
results = collection.query(
    query_texts='What is my name?',
    # n_results = 1
    )
print(results)

print("+++"*60)

collection.upsert( # updates the existing ones or inserts if doesn't exist
    documents=[
        'I live in Patna.',
        'I am aspiring data scientist.'
    ],
    ids = ['id3','id4']
)

results = collection.query(
    query_texts='Where do you live?',
    # n_results= 2
)

print(results)