from rest_framework import serializers
from .models import *

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usergroup
        fields = '__all__'
class AccessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'
class MypageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mypage
        fields = '__all__'