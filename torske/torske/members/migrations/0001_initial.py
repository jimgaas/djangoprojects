# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=40)),
                ('address2', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=30)),
                ('winteraddress1', models.CharField(max_length=40)),
                ('winteraddress2', models.CharField(max_length=40)),
                ('wintercity', models.CharField(max_length=60)),
                ('winterstate', models.CharField(max_length=30)),
                ('occupation', models.CharField(max_length=40)),
                ('businessname', models.CharField(max_length=60)),
                ('businessaddr1', models.CharField(max_length=60)),
                ('businessaddr2', models.CharField(max_length=60)),
                ('businesscity', models.CharField(max_length=30)),
                ('businessstate', models.CharField(max_length=30)),
                ('wifename', models.CharField(max_length=60)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('pic', models.ImageField(upload_to='/static/images')),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('year1', models.CharField(max_length=30)),
                ('year2', models.CharField(max_length=30)),
                ('year3', models.CharField(max_length=30)),
            ],
        ),
    ]
