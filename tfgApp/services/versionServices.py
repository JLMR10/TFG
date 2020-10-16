from tfgApp.models import Version
from tfgApp.repositories import versionRepository
from tfgApp.services import mapServices, tileListServices, chipListServices, characterListServices
import collections

def versionToJson(version):
    json = {
            "Name": version.name,
            "Map": version.map,
            "Order": version.order,
            "TileList": version.tileList,
            "ChipList": version.chipList,
            "CharacterList": version.characterList
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


def getLastVersion(mapId):
    last = 0
    lastVersion = None
    versionsIdSource = mapServices.getVersions(mapId)
    versionsSource = [versionRepository.get(id) for id in versionsIdSource]
    for version in versionsSource:
        if version["Order"] >= last:
            last = version["Order"]
            lastVersion = version
    return lastVersion


def getVersionsUpToOrder(mapId, order):
    selectedVersions = []
    versionsIdSource = mapServices.getVersions(mapId)
    versionsSource = [versionRepository.get(id) for id in versionsIdSource]
    for version in versionsSource:
        if version["Order"] <= order:
            selectedVersions.append(version)
    return selectedVersions


def createVersionFromMap(name, mapId, order, tileList, chipList, characterList):
    oldMap = getListsFromVersion(mapId, order)
    tileListId = tileListServices.newTileList(oldMap[0], tileList)
    chipListId = chipListServices.newChipList(oldMap[1], chipList)
    characterListId = characterListServices.newCharacterList(oldMap[2], characterList)
    _,versionId = createVersion(name, mapId, order + 1, tileListId, chipListId, characterListId)
    return versionId


def createVersion(name, mapId, order, tileList, chipList, characterList):
    versionDB = Version(name + "_" + str(order), mapId, order, tileList, chipList, characterList)
    versionJson = versionToJson(versionDB)
    message, versionId = versionRepository.create(versionJson)
    return message, versionId


def createFirstVersionForNewMap(sourceMapId, mapName, mapId):
    versionsIdSource = mapServices.getVersions(sourceMapId)
    versionsSource = [versionRepository.get(id) for id in versionsIdSource]
    mergedTileListId = mergeVersionsTileLists(versionsSource)
    mergedChipListId = mergeVersionsChipLists(versionsSource)
    mergedCharacterListId = mergeVersionsCharacterLists(versionsSource)
    _, versionId = createVersion(mapName + "_0", mapId, 0, mergedTileListId, mergedChipListId, mergedCharacterListId)
    mapServices.addInitialVersion(versionId, mapId)


def getListsFromVersion(mapId, maxOrder):
    versionsId = mapServices.getVersions(mapId)
    versions = [versionRepository.get(id) for id in versionsId]
    tileList = getVersionsTileLists(versions, maxOrder)
    chipList = getVersionsChipLists(versions, maxOrder)
    characterList = getVersionsCharacterLists(versions, maxOrder)
    return [tileList, chipList, characterList]


def getVersionsTileLists(versions, maxOrder):
    tileListOrderedDict = collections.OrderedDict(sorted({version["Order"]: version["TileList"] for version in versions}.items()))
    tileListIds = []
    for order, tileListId in tileListOrderedDict.items():
        if order <= maxOrder:
            tileListIds.append(tileListId)
    mergeTileList = tileListServices.mergeTileList(tileListIds)
    return mergeTileList


def getVersionsChipLists(versions, maxOrder):
    chipListOrderedDict = collections.OrderedDict(
        sorted({version["Order"]: version["ChipList"] for version in versions}.items()))
    chipListIds = []
    for order, chipListId in chipListOrderedDict.items():
        if order <= maxOrder:
            chipListIds.append(chipListId)
    mergeChipList = chipListServices.mergeChipList(chipListIds)
    return mergeChipList


def getVersionsCharacterLists(versions, maxOrder):
    characterListOrderedDict = collections.OrderedDict(
        sorted({version["Order"]: version["CharacterList"] for version in versions}.items()))
    characterListIds = []
    for order, characterListId in characterListOrderedDict.items():
        if order <= maxOrder:
            characterListIds.append(characterListId)
    mergeCharacterList = characterListServices.mergeCharacterList(characterListIds)
    return mergeCharacterList


def mergeVersionsTileLists(versions):
    tileListOrderedDict = collections.OrderedDict(sorted({version["Order"]: version["TileList"] for version in versions}.items()))
    tileListIds = [tileListId for order, tileListId in tileListOrderedDict.items()]
    mergedTileListId = tileListServices.mergeAndCreateTileList(tileListIds)
    return mergedTileListId


def mergeVersionsChipLists(versions):
    chipListOrderedDict = collections.OrderedDict(sorted({version["Order"]: version["ChipList"] for version in versions}.items()))
    chipListIds = [chipListId for order, chipListId in chipListOrderedDict.items()]
    mergedChipListId = chipListServices.mergeAndCreateChipList(chipListIds)
    return mergedChipListId


def mergeVersionsCharacterLists(versions):
    characterListOrderedDict = collections.OrderedDict(sorted({version["Order"]: version["CharacterList"] for version in versions}.items()))
    characterListIds = [characterListId for order, characterListId in characterListOrderedDict.items()]
    mergedCharacterListId = characterListServices.mergeAndCreateCharacterList(characterListIds)
    return mergedCharacterListId


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
