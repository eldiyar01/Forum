from django.contrib import admin

from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
