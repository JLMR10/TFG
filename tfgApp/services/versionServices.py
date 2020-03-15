

def versionToJson(version):
    json = {
            "Name": version.name,
            "Map": version.map,
            "Order": version.order,
            "TileList": version.tileList
        }
    return json
