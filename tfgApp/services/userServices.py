from tfgApp.models import User


def userToJson(user):
    maps = None
    games = None
    json = '{ "' \
           '' + user.id + '": {' \
                '"Name" : ' + user.name + ',' \
                '"Email" :' + user.email + ',' \
                '"Password" :' + user.password + ',' \
                '"Maps" : {' + maps + '},' \
                '"Games" : {' + games + '}' \
                '}' \
            '}'

