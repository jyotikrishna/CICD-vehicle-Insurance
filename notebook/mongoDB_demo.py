import pandas as pd
import pymongo
import certifi
from urllib.parse import quote_plus


df = pd.read_csv('data.csv')
df.head()

data = df.to_dict(orient='records')

DB_NAME = "Proj1"
COLLECTION_NAME = "Proj1-Data"

username = quote_plus("krishjyotikrishna_db_user")
password = quote_plus("Ec7VN3nxUIdnfQMu")

CONNECTION_URL = "mongodb+srv://krishjyotikrishna_db_user:Ec7VN3nxUIdnfQMu@cluster0.jvoxbyp.mongodb.net/?appName=Cluster0"

# Create MongoDB client with SSL certificate fix
client = pymongo.MongoClient(
    CONNECTION_URL,
    tlsCAFile=certifi.where()
)

# Test connection first
client.admin.command("ping")
print("MongoDB connected successfully!")

# Select database and collection
data_base = client[DB_NAME]
collection = data_base[COLLECTION_NAME]

# Insert data
rec = collection.insert_many(data)

print(f"Inserted {len(rec.inserted_ids)} records successfully.")

