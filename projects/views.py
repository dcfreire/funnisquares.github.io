from django.shortcuts import render
#from django.http import HttpResponseRedirect
from projects.models import Project
#from .forms import ProjectForm
#from django.contrib.auth.decorators import login_required

# Create your views here.

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/single_project.html', {'project': project})

#@login_required
#def add_project(request):
#    if request.method == "POST":
#        form = ProjectForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect("../projects")
#    else:
#        form = ProjectForm()
#    return render(request, 'projects/add_project.html', {'form': form})
