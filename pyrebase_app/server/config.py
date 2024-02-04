import pyrebase
import time

config = {
    "apiKey": "AIzaSyC8PKytEbFTWyh5AUfm3IdG1_r4JOGGHA8",
    "authDomain": "akmm-photos-355b3.firebaseapp.com",
    "databaseURL" : "https://akmm-photos-355b3-default-rtdb.firebaseio.com/",
    "projectId": "akmm-photos-355b3",
    "storageBucket": "akmm-photos-355b3.appspot.com",
    "messagingSenderId": "506483991832",
    "appId": "1:506483991832:web:09a84c0f279d545f44aa6d"
};

firebase = pyrebase.initialize_app(config)
storage = firebase.database()

cloud_path = "imgs"

db = storage.child(cloud_path).get()
print(db.val())

def animate_imgs():
    keys = []
    for i in db.val():
        for j in i:
            keys.append(j)
        print(keys)
    img = db.each()
    print(img)
animate_imgs()
