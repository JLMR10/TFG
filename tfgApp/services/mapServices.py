from tfgApp.models import Map
from tfgApp.repositories import mapRepository


def mapToJson(map):
    versions = {version: True for version in map.versions}
    json = {
            "Name": map.name,
            "User": map.user,
            "Versions": versions
        }
    return json


def createMap(name, userId, versionList):
    mapDB = Map(name, userId, versionList)
    mapJson = mapToJson(mapDB)
    message, mapId = mapRepository.create(mapJson)
    return message, mapId


def addInitialVersions(versionsList, mapId):
    mapRepository.addInitialVersions(versionsList, mapId)


def getMapsForModal(userMapsDict):
    mapsModal = dict(userMapsDict)
    mapDefaultId, mapDefaultValues = mapRepository.getDefault()
    mapDefaultName = mapDefaultValues.get("Name")
    mapsModal[mapDefaultName] = mapDefaultId
    return mapsModal


def getProperty(id, propierty):
    valueFromPropierty = mapRepository.getProperty(id, propierty)
    return valueFromPropierty


def getNameFromMaps(mapsDict):
    mapsNames = {mapRepository.getProperty(key, "Name"): key for key, value in mapsDict.items()}
    return mapsNames


def getFirstVersion(id):
    firstVersionId, firstVersion = mapRepository.getFirstVersion(id)
    return firstVersionId, firstVersion

def testCreate():
    map1 = Map("testMapName2", "Jose", ["testMapName2_0"])
    map1Json = mapToJson(map1)
    message = mapRepository.create(map1Json)
    return message


def testUpdate():
    map1 = Map("testMapName2", "Jose", ["testMapName2_0"])
    map1.versions.append("testMapName2_1")
    map1Json = mapToJson(map1)
    message = mapRepository.update(map1Json)
    return message


def testDelete():
    map1 = Map("testMapName2", "Jose", ["testMapName2_0"])
    map1Json = mapToJson(map1)
    message = mapRepository.delete(map1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
