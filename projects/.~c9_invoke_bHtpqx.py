# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core import urlresolvers

# Create your models here.

class Project(models.Model):
    
    MAJOR_CHOICES = (
        ('CIVIL', 'Ingeniería civil'),
        ('ELECTRICA', 'Ingeniería eléctrica'),
        ('ELECTRONICA', 'Ingeniería electrónica'),
        ('INDUSTRIAL', 'Ingeniería industrial'),
        ('MECANICA', 'Ingeniería mecánica'),
        ('SISTEMAS', 'Ingeniería de Sistemas'),
        
    )
    
    Titulo = models.CharField(max_length=255 )
    Title = models.CharField(max_length=255)
    Resumen= models.TextField(max_length=2000)
    Abstract= models.TextField(max_length=2000)
    Imagen= models.ImageField()
    Tutores= models.CharField(max_length=255)
    Programa = models.CharField(max_length= 255, choices= MAJOR_CHOICES, default='CVL')
    def __unicode__(self):
        return self.Titulo

        return '<a href="%s"/> ' % ''
        return r(projects:details, project.id )
    admin_image.allow_tags = True
    
class User(models.Model):
    Nombres = models.CharField(max_length=255)
    Apellidos = models.CharField(max_length=255)
    Correo= models.EmailField(max_length=255)
    Codigo= models.IntegerField()
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    
    
