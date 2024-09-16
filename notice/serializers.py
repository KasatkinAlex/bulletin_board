from rest_framework import serializers

from notice.models import Ads, Comment


class AdsSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ("title", "price", "description")


class AdsSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"


class CommentSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("text", "ad")


class CommentSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
