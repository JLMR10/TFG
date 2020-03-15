from tfgApp.models import ChipList
from tfgApp.repositories import chipListRepository


def chipListToJson(chipList):
    position = {pos: name for pos, name in chipList.position}
    json = {
            "Name": chipList.name,
            "Position": position
        }
    return json


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
