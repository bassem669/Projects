from django.shortcuts import render,HttpResponse,redirect
from .models import Message,Commentre
# Create your views here.

def home(request) :
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST["email"]
        message = request.POST["message"]
        nv_message = Message(name=name,email=email,message=message)
        nv_message.save()
        return redirect('home')
    ID_Commentre = Commentre.objects.all().values_list('id', flat=True)
    
    allMessage = Message.objects.all()
    Messages = [msg for msg in allMessage if not(msg.id in ID_Commentre)]
    return render(request,'index.html',{ 'allMessage' : Messages })

def message(request,id_message) :
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST["email"]
        message = request.POST["message"]
        message_ref= Message.objects.get(id=id_message)
        nv_commentre = Commentre(name=name,email=email,message=message,message_ref=message_ref)
        nv_commentre.save()
        return redirect('message',id_message=id_message)
    message = Message.objects.get(id=id_message)
    allCommentre = Commentre.objects.filter(message_ref=message)
    return render(request,'message.html',{ 'allCommentre' : allCommentre,'message' : message})
