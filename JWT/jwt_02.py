import jwt

# Below is the json data I want to transfer securely over the internet
payload_data = {
    "name": "Dayananda D R",
    "Designation": "MTS -3",
    "Age": 33,
    "Address": "Dommaluru"
}

# Try to create a token using jwt library by passing payload data and the secret
token = jwt.encode(payload = payload_data, key="password")

print(token)

"""
Token can be transferred over the internet, 

content of the token can be pasted in jwt.io tool to decode the token.
https://jwt.io/

"""
