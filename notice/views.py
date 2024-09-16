from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from notice.models import Ads, Comment
from notice.paginators import MyPagination
from notice.serializers import AdsSerializerList, AdsSerializerCreate, CommentSerializerList, CommentSerializerCreate
from users.permissions import IsOwner, IsAdmin


class AdsListAPIView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializerList
    pagination_class = MyPagination
    filter_backends = [SearchFilter]
    search_fields = ["title", 'description', "price"]
    permission_classes = AllowAny,


class AdsCreateAPIView(generics.CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializerCreate

    def perform_create(self, serializer):
        """Автоматическое присвоение владельца обьявлению"""
        serializer.save(author=self.request.user)


class AdsRetrieveAPIView(generics.RetrieveAPIView):
    """Детальная информация."""
    queryset = Ads.objects.all()
    serializer_class = AdsSerializerList
    # permission_classes = (IsAuthenticated, IsModer | IsOwner)


class AdsUpdateAPIView(generics.UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializerCreate
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin)


class AdsDestroyAPIView(generics.DestroyAPIView):
    """Удаление"""
    queryset = Ads.objects.all()
    serializer_class = AdsSerializerList
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin)
# __________________________________________________________________________


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerList
    # pagination_class = MyPagination


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerCreate

    def perform_create(self, serializer):
        """Автоматическое присвоение владельца Отзыву"""
        serializer.save(author=self.request.user)


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    """Детальная информация."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerList
    # permission_classes = (IsAuthenticated, IsModer | IsOwner)


class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerList
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin)


class CommentDestroyAPIView(generics.DestroyAPIView):
    """Удаление"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerList
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin)
