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


def create(json, ref):
    message = "The user already exists"
    listOfUsers = []

    for id, user in database.child(ref).get().val().items():
        listOfUsers.append(user["Name"])

    if json["Name"] not in listOfUsers:
        database.child(ref).push(json)
        message = "The user has been created successfully"

    return message


def update(json, ref):
    message = "error"
    for id, user in database.child(ref).get().val().items():
        if user["Name"] == json["Name"]:
            database.child(ref + "/" + id).update(json)
            message = "Edited"
            break
    return message


def delete(json, ref):
    message = "error"
    for id, user in database.child(ref).get().val().items():
        if user["Name"] == json["Name"]:
            database.child(ref + "/" + id).remove()
            message = "Deleted"
            break
    return message

