"""
YouTube : https://www.youtube.com/watch?v=J5bIPtEbS0Q

JWT : JSon web Tokens
======================
JWT tokens are very compact way of securing messages.
It has 3 parts - header , payload and signature.

1. Header contains information regarding type and the algorithm used.
example:
{
    "type": "JWT",
    "alg:"HS256"
}


2. Payload carries information requested from end user.
example:
{
    "name": "Dayananda D R",
    "age": 33
    "Address" : "Dommaluru"
}

3. Signature - to validate Is there any tampering to original data or not


Python module needed - pyjwt


one way - we can generate the token using password  - refer jwt_02.py for more details

Another way is by using  assymetric algorithms RSA256- refer jwt_03.py for more details.
"""