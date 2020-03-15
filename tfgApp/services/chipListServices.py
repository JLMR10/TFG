from tfgApp.models import ChipList


def chipListToJson(chipList):
    position = {pos: name for pos, name in chipList.position}
    json = {
            "Name": chipList.name,
            "Position": position,
            "Name": chipList.name
        }
    return json
