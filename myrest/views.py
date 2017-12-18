from django.shortcuts import render
from django.http import HttpResponse

from myrest.permissions import IsOwnerOrReadOnly
from .models import Book
from .serializers import BookSerializer,UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from rest_framework import permissions


# Create your views here.
class BookViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # def pre_save(self,obj):
    #     obj.owner  = self.request.user

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    # def get(self, request, format=None):
    #     queryset = Book.objects.all()
    #     # serializer = BookSerializer(queryset, many=True)
    #     # return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     queryset = BookSerializer(request.DATA)
    #     if queryset.is_valid():
    #         queryset.save()
    #         return Response(queryset.data)
    #     return Response(queryset.errors)
class BookDetail(APIView):
    def get(self, request,num, format=None):
        queryset = Book.objects.get(id=num)
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

# 查看 urls.py 的 router.register(r'booklist', views.Booklist)
class Booklist(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

