import chromadb as cdb

client = cdb.EphemeralClient()

collection = client.create_collection(name='storage_1')
collection2 = client.create_collection(name='storage_2')
collection3 = client.create_collection(name='storage_3')

collection.upsert(
    documents=[
        'My name is Aarush Singh.',
        'I am learning data science.',
        "I belong to Bihar, India.",
        "I live in Patna."
    ],
    ids=['id1','id2','id3','id4'],
    metadatas=[
        {'aim':'learn vector databse handling using chromadb'},
        {'location':'patna'},
        {'year':2025},
        {'college':'mca under patna university'}
    ]
)

collection2.upsert(
    documents=[
        'My name is Rahul Kumar.',
        'I live in Sheikhpura, Bihar, India.',
        'I am studying in 3rd standard.',
        'I like to draw and paint.'
    ],
    ids = [f'id{i}' for i in range(1,5)]
)

collection3.upsert(
    documents=[
        'My name is Abhishek Arya.',
        'I live in Patna, India.',
        'I study in LMC.',
        'I am 14 years old.'
    ],
    ids = [f'id{i}' for i in range(1,5)]
)

# print(dir(collection))
# print(client.list_collections())
# print(collection.peek()) # returns the first 10 records.
print(collection.count()) # returns the number of records