from tfgApp.repositories import userRepository, versionRepository
from tfgApp.services import mapServices
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
    id = ""
    userMaps = userRepository.getMaps(json["User"])
    userMapsNames = []
    if userMaps:
        userMapsNames = mapServices.getNameFromMaps(userMaps)
    if json["Name"] not in userMapsNames:
        obj = database.child(ref).push(json)
        id = obj["name"]
        message = "The map has been created successfully"

    return message, id


def getDefault():
    obj = database.child(ref+"/-M2UkUrIG3GC19lqpJD1").get()
    return obj.query_key, obj.val()


def get(id):
    return database.child(ref+"/"+id).get().val()


def getProperty(id, propierty):
    return database.child(ref+"/"+id).get().val().get(propierty)


def getFirstVersion(id):
    versions = database.child(ref+"/"+id).get().val().get("Versions")
    firstVersion = None
    firstVersionId = None
    for versionId, _ in versions.items():
        version = versionRepository.get(versionId)
        order = version["Order"]
        if order == 0:
            firstVersion = version
            firstVersionId = versionId
    return firstVersionId, firstVersion


def getVersions(id):
    versions = list(database.child(ref + "/" + id).get().val().get("Versions").keys())
    return versions


def addInitialVersion(versionId, mapId):
    versionsJson = {"Versions": {versionId: "true"}}
    reference = ref + "/" + mapId
    database.child(reference).update(versionsJson)


def addVersion(versionId, mapId):
    versionsJson = {versionId: "true"}
    reference = ref + "/" + mapId + "/Versions/"
    mapVersions = database.child(reference).get().val()
    if mapVersions:
        database.child(reference).update(versionsJson)
    else:
        versionsJson = {"Versions": versionsJson}
        database.child(reference).update(versionsJson)


"""mapJson = {mapId: "true"}
    reference = ref + "/" + userId + "/Maps/"
    userMaps = database.child(reference).get().val()
    if userMaps:
        database.child(reference).update(mapJson)
    else:
        mapsJson = {"Maps": mapJson}
        database.child(reference).update(mapJson)"""


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
