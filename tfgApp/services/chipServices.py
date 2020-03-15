from tfgApp.models import Chip
from tfgApp.repositories import chipRepository


def chipToJson(chip):
    json = {
            "Game" : chip.game,
            "MoveStat" : chip.moveStat,
            "Name" : chip.name
        }
    return json


def testCreate():
    chip1 = Chip("autoTestChip0", "0", "autoTestGame")
    chip1Json = chipToJson(chip1)
    message = chipRepository.create(chip1Json)
    return message


def testUpdate():
    chip1 = Chip("autoTestChip", "0", "autoTestGame")
    chip1.moveStat = 1
    chip1Json = chipToJson(chip1)
    message = chipRepository.update(chip1Json)
    return message


def testDelete():
    chip1 = Chip("autoTestChip", "0", "autoTestGame")
    chip1Json = chipToJson(chip1)
    message = chipRepository.delete(chip1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())