# Generated by Django 3.2.7 on 2021-09-19 13:15

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.CharField(default=core.models.generate_nanoid, max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.CharField(default=core.models.generate_nanoid, max_length=30, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=255)),
                ('faviconUrl', models.CharField(blank=True, max_length=255, null=True)),
                ('tags', models.ManyToManyField(to='links.Tag')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
