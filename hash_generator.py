import hashlib

def hash_file(filename):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    try:
        # 'rb' means Read Binary (required for photos, PDFs, etc.)
        with open(filename, "rb") as f:
            # Read the file in 4KB chunks
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "\033[91mError: File not found.\033[0m"

print("--- Hilda's Tech Haven: File Integrity Auditor ---")
file_to_check = input("Enter the full name of the file (e.g., photo.jpg): ")

result = hash_file(file_to_check)

print(f"\n\033[92mSHA-256 File Hash:\033[0m {result}")