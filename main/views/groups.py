from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from main.models.groups import Group
from main.serializers.groups import GroupSerializer


class GroupView(GenericAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all()

    def get(self, request, category_id, *args, **kwargs):
        gorups = Group.objects.filter(category_id=category_id)
        serializer = GroupSerializer(gorups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

