from django.shortcuts import render, redirect
from .models import *
from .models import Image as imgmodel
from django.core.files.images import ImageFile
from django.core.files import File
from django.contrib import messages
from image.aes import *
from image.divide import *
from image.concatenate import *
from audio.divideaudio import *
from audio.aes import *
from audio.concatenateaudio import *
from audio.stego_encode import *
from audio.stego_decode import *
import random
# Create your views here.


def home(request):
    return render(request, 'home.html')

def imagehome(request):
    return render(request, "imagehome.html")

def putdataimage(request):
    if request.method=="POST":
        # image_id=request.POST["image_id"]
        image=request.FILES["image"]
        pt=request.POST["pt"]
        pw=request.POST["pw"]
        try:
            imgmodel.objects.create(image_id=1, image=image)
            getimage=imgmodel.objects.get(image_id=1)
            print("media/"+str(getimage.image))
            src="media/"+str(getimage.image)
            a(pt, pw, src, src)
            print("lol")
            left, right=divfunc(src)
            id=random.randint(1, 499)
            id2=id+random.randint(1, 499)
            ids=list(imgmodel.objects.all().values_list('image_id', flat=True)) 
            while(id in ids and id2 in ids):
                id=random.randint(1, 499)
                id2=id+random.randint(1, 499)
            print(id, id2)
            imgmodel.objects.create(image_id=id, image=ImageFile(open(left, "rb")))
            imgmodel.objects.create(image_id=id2, image=ImageFile(open(right, "rb")))
            getimage.delete()
            return render(request, "noteidsimage.html", locals())
        except:
            return redirect("error")
    return render(request, 'putdataimage.html')

def getdataimage(request):
    images=imgmodel.objects.all()
    if request.method=="POST":
        pw=request.POST["pw"]
        left_id=request.POST["left"]
        right_id=request.POST["right"]
        left_image=imgmodel.objects.get(image_id=left_id)
        right_image=imgmodel.objects.get(image_id=right_id)
        left_src="media/"+str(left_image.image)
        right_src="media/"+str(right_image.image)
        concatfunc(left_src, right_src)
        pt=b("media/joined.png", pw)
        return render(request, "showdataimage.html", locals())
    return render(request, "getdataimage.html", locals())

def error(request):
    return render(request, "error.html")

def audiohome(request):
    return render(request, "audiohome.html")

def putdataaudio(request):
    if request.method=="POST":
        # image_id=request.POST["image_id"]
        audio=request.FILES["audio"]
        pt=request.POST["pt"]
        pw=request.POST["pw"]
        try:
            Audio.objects.create(audio_id=1, audio=audio)
            getaudio=Audio.objects.get(audio_id=1)
            # print("media/"+str(getaudio.audio))
            src="media/"+str(getaudio.audio)
    #         print(src[:-4])
            x(pt, pw, src, src)

            divfuncaudio(src)
            id=random.randint(1, 499)
            id2=id+random.randint(1, 499)
            ids=list(Audio.objects.all().values_list('audio_id', flat=True)) 
            while(id in ids and id2 in ids):
                id=random.randint(1, 499)
                id2=id+random.randint(1, 499)
            print(id, id2)
            Audio.objects.create(audio_id=id, audio=File(open(src[:-4]+"left.wav", "rb")))
            Audio.objects.create(audio_id=id2, audio=File(open(src[:-4]+"right.wav", "rb")))
            getaudio.delete()
            return render(request, "noteidsaudio.html", locals())
        except:
            return redirect("error")
    return render(request, "putdataaudio.html", locals())

def getdataaudio(request):
    audios=Audio.objects.all()
    if request.method=="POST":
        pw=request.POST["pw"]
        left_id=request.POST["left"]
        right_id=request.POST["right"]
        left_audio=Audio.objects.get(audio_id=left_id)
        right_audio=Audio.objects.get(audio_id=right_id)
        left_src="media/"+str(left_audio.audio)
        right_src="media/"+str(right_audio.audio)
        concatfuncaudio(left_src, right_src)
        pt=y("media/joined.wav", pw)
        return render(request, "showdataaudio.html", locals())
    return render(request, "getdataaudio.html", locals())