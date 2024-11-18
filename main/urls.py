from django.urls import path
from main.views.categories import CategoryListAPIView
from main.views.groups import GroupView

urlpatterns = [
    path('add-group', GroupView.as_view(), name='add_group'),
    path('groups-by-category/<int:category_id>', GroupView.as_view(), name='groups_by_category'),

    path('categories-list', CategoryListAPIView.as_view(), name='categories_list'),
]
