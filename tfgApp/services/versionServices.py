from tfgApp.models import Version
from tfgApp.repositories import versionRepository
from tfgApp.services import mapServices, tileListServices
import collections

def versionToJson(version):
    json = {
            "Name": version.name,
            "Map": version.map,
            "Order": version.order,
            "TileList": version.tileList
        }
    return json


def create(json):
    message, versionId = versionRepository.create(json)
    return message, versionId


def get(id):
    version = versionRepository.get(id)
    return version


def getPropierty(id, propierty):
    valueFromPropierty = versionRepository.getPropierty(id, propierty)
    return valueFromPropierty


def createVersion(name, mapId, order, tileList):
    versionDB = Version(name, mapId, order, tileList)
    versionJson = versionToJson(versionDB)
    message, versionId = versionRepository.create(versionJson)
    return message, versionId


def createFirstVersionForNewMap(sourceMapId, mapName, mapId):
    versionsIdSource = mapServices.getVersions(sourceMapId)
    versionsSource = [versionRepository.get(id) for id in versionsIdSource]
    mergedTileListId = mergeVersionsTileLists(versionsSource)
    _, versionId = createVersion(mapName + "_0", mapId, 0, mergedTileListId)
    mapServices.addInitialVersion(versionId, mapId)


def mergeVersionsTileLists(versions):
    tileListOrderedDict = collections.OrderedDict(sorted({version["Order"]: version["TileList"] for version in versions}.items()))
    tileListIds = [tileListId for order, tileListId in tileListOrderedDict.items()]
    mergedTileListId = tileListServices.mergeAndCreateTileList(tileListIds)
    return mergedTileListId


def testCreate():
    version1 = Version("testMapName_1", "testMapName", "1", "testTileListName")
    version1Json = versionToJson(version1)
    message = versionRepository.create(version1Json)
    return message


def testUpdate():
    version1 = Version("testMapName_1", "testMapName", "1", "testTileListName")
    version1.tileList = "testTileListNameEdited"
    version1Json = versionToJson(version1)
    message = versionRepository.update(version1Json)
    return message


def testDelete():
    version1 = Version("testMapName_1", "testMapName", "1", "testTileListName")
    version1Json = versionToJson(version1)
    message = versionRepository.delete(version1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
