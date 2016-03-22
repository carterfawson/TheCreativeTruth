from django.db import models
import datetime

class post(models.Model):
    postid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    createdate = models.DateField(default=datetime.datetime.now().date())
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    authorid = models.ForeignKey('author')

class author(models.Model):
    authorid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    position = models.CharField(max_length=45)

class comments(models.Model):
    cmtid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    postid = models.ForeignKey('post')
    content = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

class replies(models.Model):
    replyid = models.AutoField(primary_key=True)
    parentid = models.ForeignKey('comments')
    #parentid = models.IntegerField(null=False)
    name = models.CharField(max_length=250)
    content = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    #I am thinking that for this, if it is 1 then this is a reply to a comment. If it is a zero then this is a reply to another reply. This is the way that we will be able to load them in.
    #parent_type = models.IntegerField()





