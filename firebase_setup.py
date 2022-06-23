from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('./creds.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
firebase = firebase.FirebaseApplication('https://srappinp.firebaseio.com', None)

def post(data):
    db.collection('sipp').add(data)

def get():
    data = db.collection('sipp').document('1iBQiVL0DbPfVSTWgdWQ').get()
    return data.to_dict()

def get_all():
    data = db.collection('sipp').stream()
    for dat in data :
        dict = dat.to_dict()
        print(dict['nomor-perkara'])