from django.shortcuts import render
from projects.models import projects
# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'portfolio.html', context)