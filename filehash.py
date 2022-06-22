import hashlib

md5_hash = hashlib.md5()

with open("fib.py", 'rb') as f:
    content = f.read()

# print(content)

md5_hash.update(content)
digest = md5_hash.hexdigest()
print("DIGEST: ", digest)
