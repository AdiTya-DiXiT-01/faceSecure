from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserProfile
from django.contrib import messages
from Face_Detection.detection import FaceRecognition

faceRecognition = FaceRecognition()


def home(request):
    return render(request, 'faceDetection/home.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully registered")
            addFace(request.POST['face_id'])
            return redirect('home')
        else:
            messages.error(request, "Registration failed")
    else:
        form = RegistrationForm()

    return render(request, 'faceDetection/register.html', {'form': form})


def addFace(face_id):
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()


def login(request):
    face_id = faceRecognition.recognizeFace()
    return redirect('greeting', face_id=face_id)


def greeting(request, face_id):
    face_id = int(face_id)
    user = UserProfile.objects.get(face_id=face_id)
    context = {
        'user': user
    }
    return render(request, 'faceDetection/greeting.html', context=context)
