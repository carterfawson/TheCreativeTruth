from django.contrib import admin
from .models import replies, comments, author, post

admin.site.register(replies)
admin.site.register(comments)
admin.site.register(author)
admin.site.register(post)
# Register your models here.
