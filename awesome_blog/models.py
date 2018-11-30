from django.db import models
import django.utils.timezone as timezone
import time, uuid


# Create your models here.

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=next_id())
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32, null=True)
    gmt_created = models.DateTimeField(default=timezone.now)
    gmt_updated = models.DateTimeField(auto_now=True)


class Blog(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=next_id())
    user_id = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    title = models.TextField(max_length=50)
    summary = models.TextField(max_length=100, null=True)
    content = models.TextField(max_length=500, null=True)
    gmt_created = models.DateTimeField(default=timezone.now)
    gmt_updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=next_id())
    blog_id = models.CharField(max_length=32)
    user_id = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    content = models.TextField(max_length=500)
    gmt_created = models.DateTimeField(default=timezone.now)
    gmt_updated = models.DateTimeField(auto_now=True)
