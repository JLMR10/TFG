from django.db import models

# Create your modelClasses here.


class User:
    def __init__(self, name, email, password, maps, games):
        self.name = name
        self.email = email
        self.password = password
        self.maps = maps
        self.games = games


class Map:
    def __init__(self, name, user, versions):
        self.name = name
        self.user = user
        self.versions = versions


class Game:
    def __init__(self, name, code, map, chipList):
        self.name = name
        self.code = code
        self.map = map
        self.chipList = chipList


class Chip:
    def __init__(self, game, moveStat, name):
        self.name = name
        self.game = game
        self.moveStat = moveStat


class ChipList:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Tile:
    def __init__(self, image, name):
        self.image = image
        self.name = name


class TileList:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Version:
    def __init__(self, map, order, tileList):
        self.map = map
        self.order = order
        self.tileList = tileList

