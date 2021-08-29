import json
import datetime
import time
import requests

from google.auth import crypt
from google.auth import jwt
import google.auth.crypt.rsa
import google.auth.jwt


project = '<Project Name>'
key_file= '<keyFile>'
scope = 'https://www.googleapis.com/auth/cloud-platform'
#Time in seconds
expirytime= 3000

def load_json():
    with open(key_file, 'r') as key:
        data = key.read()
    return  json.loads(data)

def jwt_create():
    print('JWT Create')
    keydata = load_json()

    privateKey = keydata['private_key']
    saemail = keydata['client_email']
    aud = keydata['token_uri']
    encryptAlgo = "RS256"
    #now = datetime.datetime.utcnow() expirytime = now + datetime.timedelta(minutes=60)
    currettime = int(time.time())
    exp = currettime + expirytime

    print(f'{exp} ')

    payload = {
        'iat': currettime,
        'exp': exp,
        'iss': saemail,
        'aud': aud,
        'sub': saemail,
        'email': saemail,
        'scope': scope
    }

    signer = google.auth.crypt.RSASigner.from_service_account_file(key_file)
    jwttext = google.auth.jwt.encode(signer, payload)

    params = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwttext
    }
    auth_url = "https://www.googleapis.com/oauth2/v4/token"
    r = requests.post(auth_url, data=params)

    if r.ok:
        print(f"Token received successfully{r.text}")
    else:
        print(f"error {r.text}")


jwt_create()
