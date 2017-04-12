# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('alt', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='session',
            name='student',
            field=models.ManyToManyField(to='api.Student'),
        ),
        migrations.AddField(
            model_name='question',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Session'),
        ),
        migrations.AddField(
            model_name='professor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Option'),
        ),
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Student'),
        ),
    ]
