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

ref = "TileList"


def create(json):
    tileList = database.child(ref).push(json)
    tileListId = tileList["name"]
    message = "The tileList has been created successfully"

    return message, tileListId


def get(id):
    tileList = database.child(ref + "/" + id).get().val()
    return tileList


def getPropierty(id, propierty):
    valueFromPropierty = database.child(ref + "/" + id).get().val().get(propierty)
    if propierty == "Position":
        valueFromPropiertyFormatted = {}
        for position, tile in valueFromPropierty.items():
            position = position.replace("_", "")
            valueFromPropiertyFormatted[position] = tile
    return valueFromPropiertyFormatted


def update(json):
    message = "The tileList hasn't been edited"
    for id, tileList in database.child(ref).get().val().items():
        if tileList["Name"] == json["Name"]:
            database.child(ref + "/" + id).update(json)
            message = "The tileList has been edited successfully"
            break
    return message


def delete(json):
    message = "The tileList hasn't been deleted"
    for id, tileList in database.child(ref).get().val().items():
        if tileList["Name"] == json["Name"]:
            database.child(ref + "/" + id).remove()
            message = "The tileList has been deleted successfully"
            break
    return message

