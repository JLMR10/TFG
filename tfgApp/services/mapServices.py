

def mapToJson(map):
    versions = {version: True for version in map.versions}
    json = {
            "Name": map.name,
            "User": map.user,
            "Games": versions
        }
    return json
