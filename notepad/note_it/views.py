from django.shortcuts import render, redirect
from .models import Note
# Create your views here.

def editNote(request,note_id):
    obj = Note.objects.get(id=note_id)
    context ={
        'obj' : obj
    }
    return render(request,'editNote.html',context)

def editedNote(request,note_id):
    if request.method == 'POST':
        obj = Note.objects.get(id=note_id)
        obj.title = request.POST['title']
        obj.desc    = request.POST['desc']
        obj.save()
    return redirect('/')



def deleteNote(request,note_id):
    obj = Note.objects.get(id=note_id)
    obj.delete()
    return redirect('/')

def createNote(request):
    if request.user.is_authenticated == False:
        return redirect('/')
    if request.method == 'POST':
        t = request.POST['title']
        d = request.POST['desc']
        user = request.user
        Note.objects.create(title = t , desc = d , owner = user)
    return redirect('/')


def addNote_view(request):
    obj = Note()
    obj.title = 'Title'
    obj.desc = 'Description'
    context = {
        'obj' : obj
    }
    return render(request,'addNote.html',context)

def note_view(request):
    obj = Note.objects.filter(owner = request.user)
    context = {
        'obj' : obj
    }
    return render(request,'home.html',context)