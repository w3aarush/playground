import chromadb as db
import pandas as pd

# loading data from csv file
chat_data = pd.read_csv('./chatdata.csv')

persistent_client = chromadb.Persistent