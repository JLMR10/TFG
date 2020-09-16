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

ref = "Game"


def create(json):
    message = "The game name already exists"
    listOfGames = []

    for id, game in database.child(ref).get().val().items():
        listOfGames.append(game["GameName"])

    if json["GameName"] not in listOfGames:
        database.child(ref).push(json)
        message = "The game has been created successfully"

    return message


def get(id):
    return database.child(ref+"/"+id).get().val()


def getProperty(id, propierty):
    return database.child(ref+"/"+id).get().val().get(propierty)


def update(json):
    message = "The game hasn't been edited"
    for id, game in database.child(ref).get().val().items():
        if game["GameName"] == json["GameName"]:
            database.child(ref + "/" + id).update(json)
            message = "The game has been edited successfully"
            break
    return message


def delete(json):
    message = "The game hasn't been deleted"
    for id, game in database.child(ref).get().val().items():
        if game["GameName"] == json["GameName"]:
            database.child(ref + "/" + id).remove()
            message = "The game has been deleted successfully"
            break
    return message

