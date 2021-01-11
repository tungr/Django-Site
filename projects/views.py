from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all() # Query objects from Project database table
    context = { # Send information from query to the template
        'projects': projects
    }
    return render(request, 'project_index.html', context) # Makes objects in query available (rendered) to the template on the page

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) # Querues project with primary key (pk)
    context = {
        'project': project # Assign project to context
    }
    return render(request, 'project_detail.html', context)

