# eventures/serializers.py

from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Customize token claims
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'first_name', 'last_name', 'user_type',)


class StudentSerializer(serializers.ModelSerializer):
    user = MyUserSerializer()

    class Meta:
        model = Student
        fields = ('id', 'user', 'first_name', 'last_name',)


class OrganizationSerializer(serializers.ModelSerializer):
    user = MyUserSerializer()

    class Meta:
        model = Organization
        fields = ('id', 'user', 'org_name',)


# from rest_framework import serializers
# from .models import *
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Customize token claims
#         token['email'] = user.email
#         token['first_name'] = user.first_name
#         token['last_name'] = user.last_name

#         return token


# class MyUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = ('id', 'email', 'first_name', 'last_name', 'city',
#                   'phone', 'allergies', 'drinking_preferences',)
#         # 'event_name','event_committee_name', 'event_description', 'event_date', 'event_ticket_release_date', 'event_location', 'event_price')


# class OrganizationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Organization
#         fields = ('id', 'event_name', 'event_committee_name', 'event_description',
#                   'event_date', 'event_ticket_release_date', 'event_location', 'event_price')
