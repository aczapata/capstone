# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-18 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20160418_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='major',
            field=models.CharField(choices=[('CVL', 'Ingenieria civil'), ('ELC', 'Ingenieria electrica'), ('ELT', 'Ingenieria electronica'), ('IND', 'Ingenieria industrial'), ('MEC', 'Ingenieria mecinica'), ('SIS', 'Ingenieria de Sistemas')], default='SIS', max_length=255),
        ),
    ]
