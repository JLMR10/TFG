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
