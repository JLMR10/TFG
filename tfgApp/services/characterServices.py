from tfgApp.models import Character
from tfgApp.repositories import characterRepository


def characterToJson(character):
    json = {
            "Image": character.image,
            "Name": character.name
        }
    return json


def getAllCharacters():
    listOfCharacters = []
    sourceCharacters = characterRepository.getAllCharacters()
    for id, character in sourceCharacters:
        listOfCharacters.append([id, character["Image"]])

    return listOfCharacters


def testCreate():
    character1 = Character("mokutonImageRef", "mokuton")
    character1Json = characterToJson(character1)
    message = characterRepository.create(character1Json)
    return message


def testUpdate():
    character1 = Character("mokutonImageRef", "mokuton")
    character1.image = "dotonImageRef"
    character1Json = characterToJson(character1)
    message = characterRepository.update(character1Json)
    return message


def testDelete():
    character1 = Character("mokutonImageRef", "mokuton")
    character1Json = characterToJson(character1)
    message = characterRepository.delete(character1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
