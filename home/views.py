from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Homes
from django.urls import reverse


# Create your views here.
def index(request):
    myHomes = Homes.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'myHomes' : myHomes,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addStudent(request):
    a = request.POST['fname']
    b = request.POST['lname']
    c = request.POST['depname']
    d = request.POST['gpa']
    home = Homes(fname=a, lname=b, depname=c, gpa=d)
    home.save()
    return HttpResponseRedirect(reverse('index'))

def delData(request, id):
    home = Homes.objects.get(id=id)
    home.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    myHomes = Homes.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'myHomes' : myHomes,
    }
    return HttpResponse(template.render(context,request))

def updateData(request, id):
    # test git hub
    a = request.POST['fname']
    b = request.POST['lname']
    c = request.POST['depname']
    d = request.POST['gpa']
    myHomes = Homes.objects.get(id=id)
    myHomes.fname = a
    myHomes.lname = b
    myHomes.depname = c
    myHomes.gpa = d
    myHomes.save()
    return HttpResponseRedirect(reverse('index'))