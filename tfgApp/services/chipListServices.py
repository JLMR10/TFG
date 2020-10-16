from tfgApp.models import ChipList
from tfgApp.repositories import chipListRepository


def chipListToJson(chipList):
    position = {pos+"_": name for pos, name in chipList.position.items()}
    json = {
            "Position": position
        }
    return json


def create(json):
    message, tileListId = chipListRepository.create(json)
    return message, tileListId


def get(id):
    tileList = chipListRepository.get(id)
    return tileList


def getPropierty(id, propierty):
    valueFromPropierty = chipListRepository.getPropierty(id, propierty)
    return valueFromPropierty


def mergeAndCreateChipList(chipListsIds):
    chipLists = [getPropierty(id, "Position") for id in chipListsIds]
    mergedChipList = {}
    for chipList in chipLists:
        for position, chip in chipList.items():
            ##position = position.replace("_", "")
            mergedChipList[position] = chip
    mergedChipListObj = ChipList(mergedChipList)
    mergedChipListJson = chipListToJson(mergedChipListObj)
    _, mergedChipListId = create(mergedChipListJson)
    return mergedChipListId


def mergeChipList(chipListsIds):
    chipLists = [getPropierty(id, "Position") for id in chipListsIds]
    mergedChipList = {}
    for chipList in chipLists:
        for position, tile in chipList.items():
            mergedChipList[position.split("_")[0]] = tile
    return mergedChipList


def newChipList(sourceList, modifiedList):
    newList = {}
    index = 0
    for tile in modifiedList:
        if(str(index) not in sourceList.keys()):
            newList[str(index)] = tile
        elif(sourceList[str(index)] != tile):
            newList[str(index)] = tile
        index += 1
    jsonList = chipListToJson(ChipList(newList))
    _,listId = create(jsonList)
    return listId


def testCreate():
    chipList1 = ChipList("autoTestChipList", [("1-1", "NPC"), ("1-2", "NPC"), ("2-1", "NPC")])
    chipList1Json = chipListToJson(chipList1)
    message = chipListRepository.create(chipList1Json)
    return message


def testUpdate():
    chipList1 = ChipList("autoTestChipList", [("1-1", "NPC"), ("1-2", "NPC"), ("2-1", "NPC")])
    chipList1.position = [("2-1", "NPC"), ("1-4", "NPC"), ("1-3", "NPC"),("1-2", "NPC")]
    chipList1Json = chipListToJson(chipList1)
    message = chipListRepository.update(chipList1Json)
    return message


def testDelete():
    chipList1 = ChipList("autoTestChipList", [("1-1", "NPC"), ("1-2", "NPC"), ("2-1", "NPC")])
    chipList1Json = chipListToJson(chipList1)
    message = chipListRepository.delete(chipList1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
