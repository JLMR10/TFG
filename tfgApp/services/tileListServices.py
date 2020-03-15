

def tileListServices(tileList):
    position = {pos: name for pos, name in tileList.position}
    json = {
            "Name": tileList.name,
            "Position": position
        }
    return json
