from firebase import Firebase
import json
import os

from .filePaths import FBCONFIG_PATH

if FBCONFIG_PATH.exists():
    firebaseConfig = json.loads(open(FBCONFIG_PATH).read())
else :
    firebaseConfig = {
        "apiKey": os.environ["apiKey"],
        "authDomain": os.environ["authDomain"],
        "databaseURL": os.environ["databaseURL"],
        "projectId": os.environ["projetId"],
        "storageBucket": os.environ["storageBucket"],
        "messagingSenderId": os.environ["messagingSendId"],
        "appId": os.environ["appId"]
    }

firebase = Firebase(firebaseConfig)
db = firebase.database()