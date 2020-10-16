from tfgApp.models import CharacterList
from tfgApp.repositories import characterListRepository


def characterListToJson(characterList):
    position = {pos+"_": name for pos, name in characterList.position.items()}
    json = {
            "Position": position
        }
    return json


def create(json):
    message, characterListId = characterListRepository.create(json)
    return message, characterListId


def get(id):
    characterList = characterListRepository.get(id)
    return characterList


def getPropierty(id, propierty):
    valueFromPropierty = characterListRepository.getPropierty(id, propierty)
    return valueFromPropierty


def mergeAndCreateCharacterList(characterListsIds):
    characterLists = [getPropierty(id, "Position") for id in characterListsIds]
    mergedCharacterList = {}
    for characterList in characterLists:
        for position, character in characterList.items():
            ##position = position.replace("_", "")
            mergedCharacterList[position] = character
    mergedCharacterListObj = CharacterList(mergedCharacterList)
    mergedCharacterListJson = characterListToJson(mergedCharacterListObj)
    _, mergedCharacterListId = characterListRepository.create(mergedCharacterListJson)
    return mergedCharacterListId


def mergeCharacterList(characterListsIds):
    characterLists = [getPropierty(id, "Position") for id in characterListsIds]
    mergedCharacterList = {}
    for characterList in characterLists:
        for position, tile in characterList.items():
            mergedCharacterList[position.split("_")[0]] = tile
    return mergedCharacterList


def newCharacterList(sourceList, modifiedList):
    newList = {}
    index = 0
    for tile in modifiedList:
        if(str(index) not in sourceList.keys()):
            newList[str(index)] = tile
        elif(sourceList[str(index)] != tile):
            newList[str(index)] = tile
        index += 1
    jsonList = characterListToJson(CharacterList(newList))
    _,listId = create(jsonList)
    return listId


def testCreate():
    characterList1 = CharacterList("testCharacterListName2", [("1-1", "ForestTree"), ("2-1", "ForestTree"), ("2-3", "ForestTree")])
    characterList1Json = characterListToJson(characterList1)
    message, _ = characterListRepository.create(characterList1Json)
    return message


def testUpdate():
    characterList1 = CharacterList("testCharacterListName2", [("1-1", "ForestTree"), ("2-1", "ForestTree"), ("2-3", "ForestTree")])
    characterList1.position = [("1-1", "ForestTree"), ("2-1", "SimpleGrass"), ("2-3", "ForestTree")]
    characterList1Json = characterListToJson(characterList1)
    message = characterListRepository.update(characterList1Json)
    return message


def testDelete():
    characterList1 = CharacterList("testCharacterListName2", [("1-1", "ForestTree"), ("2-1", "ForestTree"), ("2-3", "ForestTree")])
    characterList1Json = characterListToJson(characterList1)
    message = characterListRepository.delete(characterList1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
