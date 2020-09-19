from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
import pyrebase
from tfgApp.models import User, Map
from tfgApp.services import userServices, mapServices, tileListServices, tileServices, versionServices, gameServices
from requests.exceptions import HTTPError
import json

## RolGameAssitant (no players)
# Create your views here.
config = {
    'apiKey': "AIzaSyAYZN2yUGa5qE3xYIEZ3eumIrWI-wkJfHI",
    'authDomain': "tfg-jlmrarl.firebaseapp.com",
    'databaseURL': "https://tfg-jlmrarl.firebaseio.com",
    'projectId': "tfg-jlmrarl",
    'storageBucket': "tfg-jlmrarl.appspot.com",
    'messagingSenderId': "1056067153172",
    'appId': "1:1056067153172:web:22af098ea407a5dc2af6601",
    'measurementId': "G-N0Q4EK399K"
}

firebase = pyrebase.initialize_app(config)

authFirebase = firebase.auth()
database = firebase.database()


def signIn(request):
    if "user" in request.session:
        return render(request, "mainMenu.html")
    else:
        if request.method == 'POST':
            email = request.POST.get("email")
            password = request.POST.get("password")

            try:
                user = authFirebase.sign_in_with_email_and_password(email, password)
            except HTTPError as e:
                error_json = e.args[1]
                message = json.loads(error_json)["error"]["message"]
                messages.error(request, message)
                return render(request, "signIn.html")

            request.session["user"] = authFirebase.current_user
            messages.success(request, "Logged successfully")
            return render(request, "mainMenu.html")
        return render(request, "signIn.html")


def logout(request):
    authFirebase.current_user = None
    del request.session["user"]
    return HttpResponseRedirect('../')


def signUp(request):
    if "user" in request.session:
        return HttpResponseRedirect('../')
    else:
        if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirmPassword = request.POST.get("confirmPassword")

            if password == confirmPassword:
                try:
                    user = authFirebase.create_user_with_email_and_password(email, password)
                except HTTPError as e:
                    error_json = e.args[1]
                    message = json.loads(error_json)["error"]["message"]
                    messages.error(request, message)
                    return render(request, "signUp.html")

                id = user['localId']
                message = userServices.createUser(id, name, email)
                messages.success(request, message)
                return HttpResponseRedirect('../')

            else:
                messages.error(request, "Passwords didn't match.")
                return render(request, "signUp.html")

        return render(request, "signUp.html")


def canvasDemo(request):
    return render(request, "canvasDemo.html")


def mainMenu(request):
    if "user" in request.session:
        return render(request, 'mainMenu.html')
    else:
        return HttpResponseRedirect('../')


def myMaps(request):
    if "user" in request.session:
        userMaps = userServices.getPropierty(request.session["user"]["localId"], "Maps")
        userMapsNames = {}
        ##res = tileListServices.mergeTileList(["-M2Ug2_ZPQV-Ch_wcnAK", "-M2Ug2_ZPQV-Ch_wcnA2", "-M2Ug2_ZPQV-Ch_wcnA3"])
        if userMaps:
            userMapsNames = mapServices.getNameFromMaps(userMaps)
        mapsModal = mapServices.getMapsForModal(userMapsNames)
        return render(request, 'myMaps.html', {"maps": userMapsNames, "mapsModal": mapsModal})
    else:
        return HttpResponseRedirect('../')


def editMap(request):
    if "user" in request.session:
        userId = request.session["user"]["localId"]
        if request.method == "POST" and "mapList" in request.POST:
            sourceMapId = request.POST.get("mapList")
            mapName = request.POST.get("mapName")
            message, mapId = mapServices.createMap(mapName, userId, [])
            versionServices.createFirstVersionForNewMap(sourceMapId, mapName, mapId)
            if message == "The map has been created successfully":
                userServices.addMap(userId, mapId)
                return render(request, "editMap.html", {"map": mapName})
            else:
                messages.error(request, message)
                return HttpResponseRedirect('../')
        if request.method == "POST" and "mapId" in request.POST:
            map = request.POST.get("mapId")
            userMaps = list(userServices.getPropierty(userId, "Maps").keys())
            if map in userMaps:
                mapName = mapServices.getProperty(map, "Name")
                return render(request, "editMap.html", {"map": mapName})
            else:
                return HttpResponseRedirect('../')
    else:
        return HttpResponseRedirect('../')


def demoChat(request, gameId):
    users = list(gameServices.getProperty(gameId, "Users").values())
    chatMessages = []
    if request.method == "POST":
        chatMessages.append(request.POST.get("newMessage"))
    return render(request, "demoChat.html", {"chatMessages": chatMessages})
