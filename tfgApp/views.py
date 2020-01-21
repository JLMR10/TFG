from django.shortcuts import render
import pyrebase
from django.contrib import auth

# Create your views here.
config = {
    'apiKey': "AIzaSyAYZN2yUGa5qE3xYIEZ3eumIrWI-wkJfHI",
    'authDomain': "tfg-jlmrarl.firebaseapp.com",
    'databaseURL': "https://tfg-jlmrarl.firebaseio.com",
    'projectId': "tfg-jlmrarl",
    'storageBucket': "tfg-jlmrarl.appspot.com",
    'messagingSenderId': "1056067153172",
    'appId': "1:1056067153172:web:22af98ea407a5dc2af6601",
    'measurementId': "G-N0Q4EK399K"
}

firebase = pyrebase.initialize_app(config)

authFirebase = firebase.auth()


def signIn(request):
    return render(request, "signIn.html")


def postsign(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        user = authFirebase.sign_in_with_email_and_password(email, password)
    except:
        message = "invalid credentials"
        return render(request, "signIn.html", {"messg": message})

    request.session["uid"] = authFirebase.current_user["idToken"]

    return render(request, "index.html", {"user": email,"messg":"logged successfully"})

def logout(request):
    return render(request,"signIn.html")
    auth.logout(request)


def canvasDemo(request):
    return render(request, "canvasDemo.html")
