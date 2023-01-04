import datetime

from flask import Flask, jsonify, request, make_response
from functools import wraps
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecret"

def verify_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify("{'Message': 'Token is Missing'}")
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except Exception as e:
            print(e)
            print("I am here")
            return jsonify('{"Message":"Token is missing or invalid"}')
        print("came out!!")
        return f(*args, **kwargs)
    return decorated

@app.route("/unprotected")
def unprotected():
    return jsonify("{'Message': 'Anyone can view this Page!!!'}")

@app.route("/protected")
@verify_token
def protected():
    return jsonify('{"Message": "Token is Valid for Valid Tokens"}')

@app.route("/login")
def login():
    auth = request.authorization
    if auth and auth.username == "dayananda" and auth.password == "pass":
        token = jwt.encode(payload={'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, key=app.config['SECRET_KEY'])
        return jsonify({'Token is  ': token})
    return make_response("Could not verify!", 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


if __name__ == "__main__":
    app.run(debug=True)