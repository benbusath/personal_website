from django.shortcuts import render
from portfolio.models import Project
from portfolio.models import Category
# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    context = {"projects": projects, "categories":categories}
    return render(request, 'portfolio.html', context)
    
def project(request, pk):
    project = Project.objects.get(pk=pk)
    project.requirements = project.requirements.splitlines()
    context = {"project":project}
    return render(request, 'project.html', context)