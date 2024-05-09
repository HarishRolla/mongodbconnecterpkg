# Import the MongoClient class from the pymongo library
from pymongo import MongoClient

# Create a MongoClient object and connect to the MongoDB server running on localhost
client = MongoClient('localhost', 27017)

# Access a specific database in the MongoDB server
db = client['mydatabase']

# Access a specific collection in the database
collection = db['mycollection']

# Insert a document into the collection
document = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
result = collection.insert_one(document)
print(f"Inserted document with ID: {result.inserted_id}")

# Query documents from the collection
query = {'city': 'New York'}
cursor = collection.find(query)

# Print each document found
for document in cursor:
    print(document)

# Close the connection to the MongoDB server
client.close()
