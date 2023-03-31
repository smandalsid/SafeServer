# AES 256 encryption/decryption using pycrypto library
 
import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
from PIL import Image
from image.stego import *
 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
 
 
def get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key
 
 
def encrypt(raw, password):
    private_key = get_private_key(password)
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf-8"))).decode("utf-8")
 
 
def decrypt(enc, password):
    private_key = get_private_key(password)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

def a(pt, pw, src, dest):
    ct=encrypt(pt, pw)
    Encode(src, ct, dest)

def b(src, pw):
    try:
        ct=Decode(src)
        return bytes.decode(decrypt(ct, pw))
    except:
        return "ianfgviuahgfvijnaerviuhnlvniaeurhvn"
        

# print("AES encryption decryption and LSB encoding decoding")
# print("Enter your choice:")
# print("1. Encrypt and Encode")
# print("2. Decode and Decrypt")

# n=int(input())
# if n==1:
#     print("Enter Source Image Path")
#     src = input()
#     print("Enter Message to Hide")
#     message = input()
#     print("Enter Destination Image Path")
#     dest = input()
#     password = input("Enter encryption password: ")
#     encrypted = encrypt(message, password)
#     print("Encrypted Message: ", encrypted)
#     print("Encoding...")
#     Encode(src, encrypted, dest)
# else:
#     print("Enter Source Image Path")
#     src = input()
#     print("Decoding...")
#     encrypted=Decode(src)
#     # print("Enter decrypted password")
#     password=input("Enter decryption password: ")
#     decrypted = decrypt(encrypted, password)
#     print(bytes.decode(decrypted))

 
# # First let us encrypt secret message



 
# # Let us decrypt using our original password


