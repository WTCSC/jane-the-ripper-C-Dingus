import hashlib

def md5(str):
    md5_hash = hashlib.md5(str.encode('utf-8'))
    return md5_hash.hexdigest()