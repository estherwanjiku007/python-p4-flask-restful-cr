from passlib.hash import pbkdf2_sha256
import hashlib,binascii,os
my_pwd="THEp_word"
hash_value=pbkdf2_sha256.hash(my_pwd)
verify=pbkdf2_sha256.verify("THEp_word",hash_value)
salt=hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
hashed_pword=hashlib.pbkdf2_hmac("sha512",my_pwd.encode("utf-8"),)