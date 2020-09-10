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

ref = "Map"


def create(json):
    message = "The map already exists"
    listOfMaps = []

    for id, map in database.child(ref).get().val().items():
        listOfMaps.append(map["Name"])

    if json["Name"] not in listOfMaps:
        id = database.child(ref).push(json)
        message = "The map has been created successfully"

    return message, id["name"]


def getDefault():
    obj = database.child(ref+"/-M2UkUrIG3GC19lqpJD1").get()
    return obj.query_key, obj.val()


def get(id):
    return database.child(ref+"/"+id).get().val()


def getProperty(id, propierty):
    return database.child(ref+"/"+id).get().val().get(propierty)


def update(json):
    message = "The map hasn't been edited"
    for id, map in database.child(ref).get().val().items():
        if map["Name"] == json["Name"]:
            database.child(ref + "/" + id).update(json)
            message = "The map has been edited successfully"
            break
    return message


def delete(json):
    message = "The map hasn't been deleted"
    for id, map in database.child(ref).get().val().items():
        if map["Name"] == json["Name"]:
            database.child(ref + "/" + id).remove()
            message = "The map has been deleted successfully"
            break
    return message


def addMapToUser(userId, mapId):
    info = {mapId: "true"}
    reference = "User/" + userId + "/Maps/"
    database.child(reference).update(info)
