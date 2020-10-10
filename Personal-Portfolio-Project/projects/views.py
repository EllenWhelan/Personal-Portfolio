from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.
def home(request):
    return render(request, 'projects/home.html')
    

def detail(request, project_id):
    project_detail=get_object_or_404(Project, pk= project_id) #primary key unique id is proj id
    return render(request,'projects/detail.html',{'project': project_detail} ) 


def proj(request):
    projects= Project.objects # gets all project objects from db 
    return render(request, 'projects/proj.html', {'projects':projects}) # passing dictionary named 'projects' of projects objs


def profile(request):
    return render(request, 'projects/profile.html')


def contact(request):
    return render(request, 'projects/contact.html')