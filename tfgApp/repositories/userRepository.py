import pyrebase

config = {
    'apiKey': "AIzaSyAYZN2yUGa5qE3xYIEZ3eumIrWI-wkJfHI",
    'authDomain': "tfg-jlmrarl.firebaseapp.com",
    'databaseURL': "https://tfg-jlmrarl.firebaseio.com",
    'projectId': "tfg-jlmrarl",
    'storageBucket': "tfg-jlmrarl.appspot.com",
    'messagingSenderId': "1056067153172",
    'appId': "1:1056067153172:web:22af098ea407a5dc2af6601",
    'measurementId': "G-N0Q4EK399K"
}

firebase = pyrebase.initialize_app(config)

database = firebase.database()

ref = "User"


def create(json, uid):
    message = "The user already exists"
    listOfUsers = []

    for id, user in database.child(ref).get().val().items():
        listOfUsers.append(user["Email"])

    if json["Email"] not in listOfUsers:
        database.child(ref).child(uid).set(json)
        message = "The user has been created successfully"

    return message


def get(id, propierty):
    return database.child(ref+"/"+id).get().val().get(propierty)


def update(json):
    message = "The user hasn't been edited"
    for id, user in database.child(ref).get().val().items():
        if user["Name"] == json["Name"]:
            database.child(ref + "/" + id).update(json)
            message = "The user has been edited successfully"
            break
    return message


def delete(json):
    message = "The user hasn't been deleted"
    for id, user in database.child(ref).get().val().items():
        if user["Name"] == json["Name"]:
            database.child(ref + "/" + id).remove()
            message = "The user has been deleted successfully"
            break
    return message


