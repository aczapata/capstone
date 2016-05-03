from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm, UserForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    projects= Project.objects.all()
    context={"projects": projects}
    return render(request, 'projects/index.html', context)
    
def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project})
    
def new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save
            print 
            num = form['team_members'].value()
            return HttpResponseRedirect(reverse('projects:team_new', args=(int(num), )))
        else:
            return HttpResponse(form.errors.as_data())
    else:
        form = ProjectForm()
        return render(request, 'projects/project_edit.html', {'form': form})

def team_new(request, num):
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('index')
        else:
            return HttpResponse(form.errors.as_data())
    else:
        form = UserForm()
        return render(request, 'projects/team_new.html', {'form': form, 'range': xrange(int(num))})
    
    