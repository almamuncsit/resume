# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-21 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='skillcategory',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='about',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='about',
            name='last_name',
            field=models.CharField(default='', max_length=250, verbose_name='Name'),
        ),
    ]