

def userToJson(user):
    maps = {map: True for map in user.maps}
    games = {game: True for game in user.games}
    json = {
            "Name": user.name,
            "Email": user.email,
            "Password": user.password,
            "Maps": maps,
            "Games": games
        }
    return json


