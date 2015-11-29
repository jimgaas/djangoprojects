# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20151127_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address1',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='member',
            name='businessaddr1',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='member',
            name='businessaddr2',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='member',
            name='businesscity',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='businessname',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='member',
            name='businessstate',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='city',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='member',
            name='email1',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='email2',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='occupation',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='wifename',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='member',
            name='winteraddress1',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='member',
            name='winteraddress2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='member',
            name='wintercity',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='member',
            name='winterstate',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='year1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='year2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='year3',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
