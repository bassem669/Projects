from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request) : 
    return render(request,'index.html')

def generate(request) :

    try : 
        if not(request.GET['length'].isdigit()) : 
            raise ValueError
    except ValueError :
        msg : str = 'la longeur doit un entier'
        return render(request,'index.html',{'msg_error' : msg})


    if int(request.GET['length']) < 8 :     
        msg : str = 'La longueur doit être supérieure à 8.'
        return render(request,'index.html',{'msg_error' : msg})
    
    import string
    import random
    lower : str = string.ascii_lowercase
    upper : str = string.ascii_uppercase
    chiffre : str = string.digits
    special : str = string.punctuation
    tout_lettre : str = lower + upper + chiffre + special
    length : int = int(request.GET['length'])
    pwd : str = ''
    for i in range(length):
        pwd += random.choice(tout_lettre)

    return render(request,'index.html',{'pwd_generated' : pwd})