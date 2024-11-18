from rest_framework.generics import ListAPIView
from main.models.categories import Category
from main.serializers.categories import CategorySerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()