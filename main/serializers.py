from rest_framework import serializers
from .models import Actor, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'birthdate', 'gender']


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'rating', 'actors']