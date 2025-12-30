import chromadb as cdb
import pandas as pd
# from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction # by default, chromadb uses this same model for embedding. so we don't need to specify here
client = cdb.Client()   # creating client

# collections to store embeddings, documents or any metadata
collection = client.create_collection(
    name='vector_db',
    embedding_function=SentenceTransformerEmbeddingFunction("sentence-transformers/all-MiniLM-L6-v2")
)

# adding some text documents to the collection
collection.add(
    ids=['id1', 'id2'],
    documents= [
        'My name is Aarush Singh.',
        "I am learning managing vector databases."
    ]
)

# querying from the database
results = collection.query(
    query_texts=['this is a query about my name'],
    n_results=2 # default value is 10
)

# displaying results
print(results)
print("="*200)
print(pd.DataFrame({'documents':results['documents'][0], 'distances':results['distances'][0]},index=results['ids'][0]))