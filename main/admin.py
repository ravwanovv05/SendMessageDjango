from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from main.models.categories import Category
from main.models.groups import Group
from main.resource import CategoryResource, GroupResource


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 10
    resource_class = CategoryResource


@admin.register(Group)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_per_page = 10
    resource_class = GroupResource