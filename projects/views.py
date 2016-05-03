from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm, UserForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import formset_factory
from django.shortcuts import render_to_response
from functools import partial, wraps
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('projects:index'))

def index(request):
    return render(request, 'projects/index.html')
    
@login_required    
def list_projects(request):
    projects= Project.objects.all()
    context={"projects": projects}
    return render(request, 'projects/list.html', context)
    
def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    users= project.user_set.all()
    return render(request, 'projects/detail.html', {'project': project, 'users': users})

def details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    users= project.user_set.all()
    return render(request, 'projects/details_complete.html', {'project': project, 'users': users})
    
def new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return HttpResponseRedirect(reverse('projects:detail', args=(project.id,)))
        else:
            return render(request, 'projects/project_edit.html', {'form': form, 'errors':form.errors.as_data() })
    else:
        form = ProjectForm()
        return render(request, 'projects/project_edit.html', {'form': form})

def edit(request, project_id=None):
    
    if project_id:
        project = get_object_or_404(Project, pk=project_id)
    else:
        project = ProjectForm()

    form = ProjectForm( request.POST or None, request.FILES or None, instance=project)
    if request.method == 'POST':
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return HttpResponseRedirect(reverse('projects:detail', args=(project.id,)))
        else:
            return render(request, 'projects/project_edit.html', {'form': form, 'errors':form.errors.as_data() })

    return render(request,'projects/project_edit.html', {'form': form, })

def new_team(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            project.user_set.create(Codigo=form['Codigo'].value(), Nombres=form['Nombres'].value(), Apellidos=form['Apellidos'].value(), Correo=form['Correo'].value())
            return HttpResponseRedirect(reverse('projects:detail', args=(project.id,)))       
        else:
            return render(request, 'projects/manage_users.html', {'form': form, 'errors':form.errors.as_data() })
    else:
        form= UserForm()
    return render(request,'projects/manage_users.html', {'form': form})

