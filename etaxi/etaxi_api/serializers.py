from rest_framework import serializers
from .models import *


class OfficeSeriazer(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = ('address',)


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name', 'position', 'quote')


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('model', 'transmission', 'engine_capacity')


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ('name', 'text')


class CitySerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True)
    offices = serializers.StringRelatedField(many=True)
    cars = CarSerializer(many=True)
    feedback = FeedbackSerializer(many=True)

    class Meta:
        model = City
        fields = ('city', 'phone', 'offices', 'team', 'cars', 'feedback')