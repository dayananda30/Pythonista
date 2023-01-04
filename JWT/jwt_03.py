"""
Here in the example I am using RSU-256 algm.
Inorder to demonstrate this, we need python cryptography module because
we are loading private key to generate token for the payload data.

"""

from cryptography.hazmat.primitives import serialization
import jwt
# load private key content to a variable
private_key = open(r"C:\Users\dayananda\.ssh\id_rsa","r").read()
print(private_key)

# creating a key similar to password I used in jwt_02.py by passing
# the content as byte string
key = serialization.load_ssh_private_key(private_key.encode(), password=b'')

print(key)

# Below is the json data I want to transfer securely over the internet
payload_data = {
    "name": "Dayananda D R",
    "Designation": "MTS -3",
    "Age": 33,
    "Address": "Dommaluru"
}

# Generate the token by passing payload data , Generated key and the algorithm used.
token = jwt.encode(payload=payload_data,
                   key=key,
                   algorithm='RS256')

print(token)