from django.db import models

# Create your modelClasses here.

class User:
    def __init__(self,id,name,email,password,maps,games):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.maps = maps
        self.games = games

