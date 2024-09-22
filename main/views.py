from django.shortcuts import render
from rest_framework import viewsets
from .models import Actor, Movie
from .serializers import ActorSerializer, MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

