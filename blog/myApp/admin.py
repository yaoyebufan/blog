from django.contrib import admin


# Register your models here.
from .models import Article,Message,comment

admin.site.register(Article)
admin.site.register(Message)
admin.site.register(comment)

