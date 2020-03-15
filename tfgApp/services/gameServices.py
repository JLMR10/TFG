from tfgApp.models import Chip


def chipToJson(chip):
    json = {
            "Game" : chip.game,
            "MoveStat" : chip.moveStat,
            "Name" : chip.name
        }
    return json