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

ref = "CharacterList"


def create(json):
    characterList = database.child(ref).push(json)
    characterListId = characterList["name"]
    message = "The characterList has been created successfully"

    return message, characterListId


def get(id):
    characterList = database.child(ref + "/" + id).get().val()
    return characterList


def getPropierty(id, propierty):
    valueFromPropierty = database.child(ref + "/" + id).get().val().get(propierty)
    if propierty == "Position":
        valueFromPropiertyFormatted = {}
        for position, character in valueFromPropierty.items():
            position = position.replace("_", "")
            valueFromPropiertyFormatted[position] = character
    return valueFromPropiertyFormatted


def update(json):
    message = "The characterList hasn't been edited"
    for id, characterList in database.child(ref).get().val().items():
        if characterList["Name"] == json["Name"]:
            database.child(ref + "/" + id).update(json)
            message = "The characterList has been edited successfully"
            break
    return message


def delete(json):
    message = "The characterList hasn't been deleted"
    for id, characterList in database.child(ref).get().val().items():
        if characterList["Name"] == json["Name"]:
            database.child(ref + "/" + id).remove()
            message = "The characterList has been deleted successfully"
            break
    return message

