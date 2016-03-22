# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('authorid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('cmtid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('postid', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('createdate', models.DateField(default=datetime.date(2016, 3, 13))),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('authorid', models.ForeignKey(to='blog.author')),
            ],
        ),
        migrations.CreateModel(
            name='replies',
            fields=[
                ('replyid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('parentid', models.ForeignKey(to='blog.comments')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='postid',
            field=models.ForeignKey(to='blog.post'),
        ),
    ]
