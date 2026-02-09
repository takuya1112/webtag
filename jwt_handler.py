import time
import jwt
from decouple import config

JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")

def token_response(token: str):
    return {
        "access token" : token
    }

def create_access_token(userID: str):
    payload = {
        "sub" : userID,
        "exp" : time.time() + 600,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decode_access_token(token : str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token["exp"] >= time.time() else None
    except:
        return {}