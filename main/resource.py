from import_export import resources

from main.models.categories import Category
from main.models.groups import Group


class CategoryResource(resources.ModelResource):
    model = Category


class GroupResource(resources.ModelResource):
    model = Group
