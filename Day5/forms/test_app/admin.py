from django.contrib import admin

# Register your models here.
from .models import Category, Page

admin.site.register(Category)
#admin.site.register(Page)

""" class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']

admin.site.register(Category,CategoryAdmin) """


class PageAdmin(admin.ModelAdmin):
    list_display=('title', 'category', 'url')

admin.site.register(Page,PageAdmin)
