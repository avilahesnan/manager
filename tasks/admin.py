from django.contrib import admin
from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ...
