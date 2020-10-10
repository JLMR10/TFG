from tfgApp.models import Tile
from tfgApp.repositories import tileRepository


def tileToJson(tile):
    json = {
            "Image": tile.image,
            "Name": tile.name
        }
    return json


def getAllTiles():
    listOfTiles = []
    sourceTiles = tileRepository.getAllTiles()
    for id, tile in sourceTiles:
        listOfTiles.append([id, tile["Image"]])

    return listOfTiles


def testCreate():
    tile1 = Tile("mokutonImageRef", "mokuton")
    tile1Json = tileToJson(tile1)
    message = tileRepository.create(tile1Json)
    return message


def testUpdate():
    tile1 = Tile("mokutonImageRef", "mokuton")
    tile1.image = "dotonImageRef"
    tile1Json = tileToJson(tile1)
    message = tileRepository.update(tile1Json)
    return message


def testDelete():
    tile1 = Tile("mokutonImageRef", "mokuton")
    tile1Json = tileToJson(tile1)
    message = tileRepository.delete(tile1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
