

def versionToJson(version):
    json = {
            "Map": version.map,
            "Order": version.order,
            "TileList": version.tileList
        }
    return json
