from rest_framework import serializers
from .models import patient,Escort,Medicine,Diseases,Document,Reminder,Register
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=False)
    username = serializers.CharField(read_only=True)


    def create(self, validated_data):
        password=validated_data.pop('password')
        user =User.objects.create(**validated_data)
        user.save()

        return user

    class Meta:
        model=User
        fields=['url','id','username','email','first_name','last_name','password']


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model= Register 
        fields="__all__"


# class LoginSerializers(serializers.ModelSerializer):
#     class Meta:
#         model= Login 
#         fields="__all__"

class pSerializers(serializers.ModelSerializer):
    class Meta:
        model= patient 
        fields="__all__"


class ESerializers(serializers.ModelSerializer):
    class Meta:
        model= Escort
        fields="__all__"


class DSerializers(serializers.ModelSerializer):
    class Meta:
        model= Diseases
        fields="__all__"


class MSerializers(serializers.ModelSerializer):
    class Meta:
        model= Medicine
        fields="__all__"


class DOSerializers(serializers.ModelSerializer):
    class Meta:
        model= Document
        fields="__all__"


class RSerializers(serializers.ModelSerializer):
    class Meta:
        model= Reminder
        fields="__all__"
