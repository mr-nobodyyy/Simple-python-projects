import hashlib
import json
import os

print("********************* FILE INTEGRITY CHECK **************************")

file_check = input("Enter the filename to check its integrity: ")

# Check if file exists
if not os.path.isfile(file_check):
    print("File does not exist.")
    exit(1)

# Compute SHA-256 
hash_obj = hashlib.sha256()
with open(file_check, "rb") as fr:
    while chunk := fr.read(4096):
        hash_obj.update(chunk)

hash_check = hash_obj.hexdigest()

# Load database
if not os.path.isfile("database.json"):
    print("database.json not found.")
    exit(1)

with open("database.json", "r") as f:
    data = json.load(f)

# Verify integrity
for entry in data:
    if entry["filename"] == file_check:
        if entry["hash"] == hash_check:
            print("OK! Hash matches. File integrity verified.")
        else:
            print("WARNING! File modified or tampered (hash mismatch).")
        break
else:
    print("File not found in database.")

print("Thank you!")
