# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-08-06 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import model_managers.interface_model_manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MockAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreationTime', models.DateTimeField(auto_now=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('ApiTitle', models.CharField(max_length=50)),
                ('ApiType', models.IntegerField()),
                ('ApiPath', models.CharField(max_length=1000)),
                ('HttpMethod', models.IntegerField()),
                ('CallBackUrl', models.CharField(max_length=500)),
                ('CallBackMethod', models.IntegerField()),
                ('MockHandler', models.IntegerField()),
                ('MockResponse', models.IntegerField()),
                ('MockServer', models.IntegerField()),
                ('MatchParten', models.CharField(max_length=20)),
                ('Enable', models.BooleanField()),
                ('Parent', models.IntegerField(default=0)),
                ('Description', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'env_mock_api',
            },
            managers=[
                ('objects', model_managers.interface_model_manager.MockAPIManager()),
            ],
        ),
        migrations.CreateModel(
            name='MockHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreationTime', models.DateTimeField(auto_now=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('HandlerName', models.CharField(max_length=100)),
                ('HandlerFile', models.CharField(max_length=100)),
                ('HandlerFileName', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'env_mock_handler',
            },
            managers=[
                ('objects', model_managers.interface_model_manager.MockHandlerManager()),
            ],
        ),
        migrations.CreateModel(
            name='MockResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreationTime', models.DateTimeField(auto_now=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('ApiID', models.IntegerField()),
                ('Response', models.CharField(max_length=100)),
                ('Enable', models.BooleanField()),
                ('Description', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'env_mock_response',
            },
            managers=[
                ('objects', model_managers.interface_model_manager.MockResponseManager()),
            ],
        ),
    ]