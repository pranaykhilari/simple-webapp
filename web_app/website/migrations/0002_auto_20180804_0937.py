# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-04 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Person',
            new_name='Father',
        ),
        migrations.AddField(
            model_name='children',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Father'),
        ),
    ]
