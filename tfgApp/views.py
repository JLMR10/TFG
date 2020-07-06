from django.shortcuts import render
import pyrebase
from tfgApp.models import User
from tfgApp.services import userServices, mapServices, tileListServices, tileServices, versionServices
from tfgApp.repositories import userRepository
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
    return render(request, "signIn.html")


def postsign(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        user = authFirebase.sign_in_with_email_and_password(email, password)
    except HTTPError as e:
        error_json = e.args[1]
        message = json.loads(error_json)["error"]["message"]
        return render(request, "signIn.html", {"messg": message})

    request.session["uid"] = authFirebase.current_user["idToken"]

    return render(request, "index.html", {"user": email, "messg": "logged successfully"})


def logout(request):
    return render(request, "signIn.html")
    auth.logout(request)


def signUp(request):
    return render(request, "signUp.html")


def postsignup(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        user = authFirebase.create_user_with_email_and_password(email, password)
    except HTTPError as e:
        error_json = e.args[1]
        message = json.loads(error_json)["error"]["message"]
        return render(request, "signUp.html", {"messg": message})

    uid = user['localId']
    userDB = User(name, email, "", ["DefaultMap1", "DefaultMap2", "DefaultMap3"], [])
    userJson = userServices.userToJson(userDB)
    message = userRepository.create(userJson, uid)

    return render(request, "signUp.html", {"messg": message})

def canvasDemo(request):
    return render(request, "canvasDemo.html")
