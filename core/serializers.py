from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = Profile
        fields = ['username', 'password']

    def create(self, data):
        user = Profile.objects.create(
            username = data['username'],
        )
        user.set_password(data['password'])
        user.save()
        return user

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class RespondSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSub
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

