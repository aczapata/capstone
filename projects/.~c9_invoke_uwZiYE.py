# -*- coding: utf-8 -*-
from django import forms
from django.forms import formset_factory
from .models import Project, User

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('Titulo','Title','Resumen', 'Abstract',  'Tutores','Programa','Imagen')
    def __init__(self, *args, **kwargs):
        self.fields['Resumen'].widget.attrs.update({'class' : 'materialize-textarea',  'length':  'id': 'textarea1', 'placeholder': 'Máximo 2000 caracteres'})
        self.fields['Resumen'].widget.attrs.update({'class' : 'materialize-textarea',  'length': 2000, 'id': 'textarea1', 'placeholder': 'Máximo 2000 caracteres incluyendo espacios'})
        self.fields['Abstract'].widget.attrs.update({'class' : 'materialize-textarea',  'length': 2000, 'id': 'textarea2','placeholder': 'Máximo 2000 caracteres incluyendo espacios'})
        
        self.fields['Titulo'].widget.attrs.update({ 'placeholder': 'Introduzca en este campo el título de su proyecto.'})
        self.fields['Title'].widget.attrs.update({ 'placeholder': 'Introduzca en este campo el título en inglés de su proyecto.'})
        self.fields['Tutores'].widget.attrs.update({ 'placeholder': 'Introduzca los nombres completos de sus tutores separados por comas'})
    def save(self, commit=True):
        return super(ProjectForm, self).save(commit=commit)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('Nombres','Apellidos','Correo', 'Codigo')
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
    def save(self, commit=True):
        return super(UserForm, self).save(commit=commit)
        