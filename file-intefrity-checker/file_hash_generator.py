import hashlib
import json
import os

file_name = input("Enter file name: ")

# Check if file exists
if not os.path.isfile(file_name):
    print(f"{file_name} file does not exist")
    exit(1)

# Initialize SHA-256
hash_object = hashlib.sha256()

# Read file in chunks
with open(file_name, "rb") as f:
    while data := f.read(4096):
        hash_object.update(data)

file_hash = hash_object.hexdigest()

file_data = {
    "filename": file_name,
    "hash": file_hash
}

# If database.json does not exist, create it
if not os.path.isfile("database.json"):
    print("database.json file not found! Creating one...")
    with open("database.json", "w") as f:
        json.dump([], f, indent=4)

# Load existing JSON data
with open("database.json", "r") as f:
    database = json.load(f)

# Append  entry # Database here is a 
database.append(file_data)


with open("database.json", "w") as f:
    json.dump(database, f, indent=4)

print(f"Data saved to database.json")
