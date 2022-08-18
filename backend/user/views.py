from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import mixins

from .models import User
from .serializers import UserModelSerializer


class UserAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @staticmethod
    def get(request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        Response(serializer.data)


class UserListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = UserModelSerializer
    queryset = User.objects.all()


class UserModelLimitedViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
