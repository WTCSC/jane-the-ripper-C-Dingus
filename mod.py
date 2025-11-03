import hashlib

def md5(str):
    md5_hash = hashlib.md5(str.encode('utf-8'))
    return md5_hash.hexdigest()

def sha1(str):
    sha1_hash = hashlib.sha1(str.encode('utf-8'))
    return sha1_hash.hexdigest()

def sha256(str):
    sha256_hash = hashlib.sha256(str.encode('utf-8'))
    return sha256_hash.hexdigest()