from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):

    dbProject = Project.objects.all()
    dbPribadi = Pribadi.objects.all()
    
    context = {
        'dbProject': dbProject,
        'dbPribadi': dbPribadi,
    }
    return render(request, 'index.html',context)