from django.contrib.auth.models import Group
from .models import User,UserPassword
from rest_framework import serializers


class UserPasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserPassword
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # userpassword = UserPasswordSerializers(many=False)
    class Meta:
        model = User
        fields = "__all__"


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']