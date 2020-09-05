from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
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
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = authFirebase.sign_in_with_email_and_password(email, password)
        except HTTPError as e:
            error_json = e.args[1]
            message = json.loads(error_json)["error"]["message"]
            messages.error(request, message)
            return render(request, "signIn.html", {})

        request.session["uid"] = authFirebase.current_user["idToken"]

        return render(request, "index.html", {"user": email, "messg": "logged successfully"})
    return render(request, "signIn.html")


def logout(request):
    authFirebase.current_user = None
    return HttpResponseRedirect('../')


def signUp(request):
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
                return render(request, "signUp.html", {})

            uid = user['localId']
            userDB = User(name, email, "", ["DefaultMap1", "DefaultMap2", "DefaultMap3"], [])
            userJson = userServices.userToJson(userDB)
            message = userRepository.create(userJson, uid)
            messages.success(request, message)
            return HttpResponseRedirect('../')

        else:
            messages.error(request,"Passwords didn't match.")
            return render(request, "signUp.html", {})

    return render(request, "signUp.html")


def canvasDemo(request):
    return render(request, "canvasDemo.html")
