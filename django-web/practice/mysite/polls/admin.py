from django.contrib import admin

# Register your models here.

# Admin 사이트에 반영
from polls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)