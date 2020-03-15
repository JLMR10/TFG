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

ref = "Chip"


def create(json):
    message = "The chip name already exists"
    listOfChips = []

    for id, chip in database.child(ref).get().val().items():
        listOfChips.append(chip["Name"])

    if json["Name"] not in listOfChips:
        database.child(ref).push(json)
        message = "The chip has been created successfully"

    return message


def update(json):
    message = "The chip hasn't been edited"
    for id, chip in database.child(ref).get().val().items():
        if chip["Name"] == json["Name"]:
            database.child(ref + "/" + id).update(json)
            message = "The game has been edited successfully"
            break
    return message


def delete(json):
    message = "The chip hasn't been deleted"
    for id, chip in database.child(ref).get().val().items():
        if chip["Name"] == json["Name"]:
            database.child(ref + "/" + id).remove()
            message = "The game has been deleted successfully"
            break
    return message

