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


def getPropierty(id, propierty):
    valueFromPropierty = database.child(ref+"/"+id).get().val().get(propierty)
    return valueFromPropierty


def getMaps(id):
    maps = database.child(ref+"/"+id).get().val().get("Maps")
    return maps


def addMap(userId, mapId):
    mapJson = {mapId: "true"}
    reference = ref + "/" + userId + "/Maps/"
    userMaps = database.child(reference).get().val()
    if userMaps:
        database.child(reference).update(mapJson)
    else:
        mapsJson = {"Maps": mapJson}
        database.child(reference).update(mapJson)


def addGameToUser(userId, gameId, gameName):
    gameJson = {gameId: gameName}
    reference = ref + "/" + userId + "/Games/"
    userGames = database.child(reference).get().val()
    if userGames:
        database.child(reference).update(gameJson)
    else:
        gamesJson = {"Games": gameJson}
        database.child(reference).update(gameJson)

"""def addMap(userId, mapId):
    info = {mapId: "true"}
    reference = ref + "/" + userId + "/Maps/"
    db = database.child(reference)
    db.child(reference).update(info)"""


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


