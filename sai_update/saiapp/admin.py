from django.contrib import admin
from .models import register1
# Register your models here.
class readmin(admin.ModelAdmin):
    list_display = ['pk','name']
admin.site.register(register1,readmin)