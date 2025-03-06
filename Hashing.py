import os
import hashlib

def hash_file(filepath):
    """Generate SHA-256 hash for a single file."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

def hash_folder(folder_path):
    """Generate a hash for the entire folder (including all files)."""
    folder_hash = hashlib.sha256()
    
    for root, dirs, files in os.walk(folder_path):
        for file in sorted(files):
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash:
                folder_hash.update(file_hash.encode('utf-8'))
    
    return folder_hash.hexdigest()

def hash_path(path):
    
    if os.path.isfile(path): # check if its a file
        return hash_file(path)
    
    elif os.path.isdir(path): # check if its a directory (folder)
        return hash_folder(path)
    
    else:
        print(f"The path '{path}' is neither a file nor a directory.")
        return None


while True:
    path = input("Enter the path to file or folder (or type 'exit' to quit): ")
    
    if path.lower() == 'exit':
        print("Exiting the program.")
        break 
    
    result = hash_path(path)
    
    if result:
        print(f"Hash for '{path}': {result}")
    else:
        print(f"Could not compute hash for '{path}'. Please check the path and try again.")


