from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Job)

admin.site.register(Application)
admin.site.register(Test)
admin.site.register(Question)