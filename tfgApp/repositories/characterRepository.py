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

ref = "Character"


def create(json):
    message = "The character already exists"
    listOfCharacter = []

    for id, character in database.child(ref).get().val().items():
        listOfCharacter.append(character["Name"])

    if json["Name"] not in listOfCharacter:
        database.child(ref).push(json)
        message = "The characterList has been created successfully"

    return message


def getAllCharacters():
    return database.child(ref).get().val().items()


def update(json):
    message = "The character hasn't been edited"
    for id, character in database.child(ref).get().val().items():
        if character["Name"] == json["Name"]:
            database.child(ref + "/" + id).update(json)
            message = "The character has been edited successfully"
            break
    return message


def delete(json):
    message = "The character hasn't been deleted"
    for id, character in database.child(ref).get().val().items():
        if character["Name"] == json["Name"]:
            database.child(ref + "/" + id).remove()
            message = "The character has been deleted successfully"
            break
    return message

