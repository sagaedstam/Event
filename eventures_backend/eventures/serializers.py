# eventures/serializers.py
from rest_framework import serializers
from .models import MyUser, Student, Organization


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'date_joined', 'is_staff', 'is_active', 'user_type')


class StudentSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(required=True)

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'user')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = MyUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        student = Student.objects.create(user=user, **validated_data)

        return student



class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'org_name')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'email', 'password', 'user_type')

    def create(self, validated_data):
        user = MyUser.objects.create(
            email=validated_data['email'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
