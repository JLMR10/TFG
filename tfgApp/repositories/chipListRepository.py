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

ref = "ChipList"


def create(json):
    message = "The chipList name already exists"
    listOfChipLists = []

    for id, chipList in database.child(ref).get().val().items():
        listOfChipLists.append(chipList["Name"])

    if json["Name"] not in listOfChipLists:
        database.child(ref).push(json)
        message = "The chipList has been created successfully"

    return message


def update(json):
    message = "The chipList hasn't been edited"
    for id, chipList in database.child(ref).get().val().items():
        if chipList["Name"] == json["Name"]:
            database.child(ref + "/" + id).update(json)
            message = "The chipList has been edited successfully"
            break
    return message


def delete(json):
    message = "The chipList hasn't been deleted"
    for id, chipList in database.child(ref).get().val().items():
        if chipList["Name"] == json["Name"]:
            database.child(ref + "/" + id).remove()
            message = "The chipList has been deleted successfully"
            break
    return message

