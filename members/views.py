from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users
# Create your views here.

def members(request):
    #return HttpResponse("Hello world!")
     #template =loader.get_template('index.html')
     # return HttpResponse(template.render())
    mymembers=Users.objects.all().values()
    template =loader.get_template('members.html')
    context ={
        'mymembers':mymembers,
    }
  
    return HttpResponse(template.render(context, request))
