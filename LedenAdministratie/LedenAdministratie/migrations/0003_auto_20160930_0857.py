# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 06:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LedenAdministratie', '0002_auto_20160918_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lid',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('read_lid', 'Can read leden'),), 'verbose_name_plural': 'Leden'},
        ),
    ]
