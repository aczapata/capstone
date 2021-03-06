# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-18 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20160330_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='major',
            field=models.CharField(choices=[(b'SIS', b'Ing. de Sistemas')], default=b'SIS', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='abstract',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='project',
            name='abstract_en',
            field=models.TextField(max_length=2000),
        ),
    ]
