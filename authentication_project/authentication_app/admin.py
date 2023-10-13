from django.contrib import admin
from .models import Goal

# Register your models here.
@admin.register(Goal)
class Admingoals(admin.ModelAdmin):
    list_display=['id','user','title','description']
    search_fields=['id','user']