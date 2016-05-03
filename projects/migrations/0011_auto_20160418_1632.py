# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-18 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160418_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='abstract',
            new_name='Abstract',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='abstract_en',
            new_name='Resumen',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='advisor',
            new_name='Titulo',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title_en',
            new_name='Tutores',
        ),
        migrations.RemoveField(
            model_name='project',
            name='major',
        ),
        migrations.AddField(
            model_name='project',
            name='Programa',
            field=models.CharField(choices=[('CVL', 'Ingenieria civil'), ('ELC', 'Ingenieria electrica'), ('ELT', 'Ingenieria electronica'), ('IND', 'Ingenieria industrial'), ('MEC', 'Ingenieria mecinica'), ('SIS', 'Ingenieria de Sistemas')], default='CVL', max_length=255),
        ),
    ]