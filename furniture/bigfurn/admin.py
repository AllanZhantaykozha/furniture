from django.contrib import admin
from .models import *


class BigfurnAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'company')
    fields = ('title', 'content', 'photo', 'company', 'category', 'contact', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    fields = ('title', )


admin.site.register(Bigfurn, BigfurnAdmin)
admin.site.register(Category, CategoryAdmin)
