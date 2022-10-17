from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import render
from functools import partial
from django.shortcuts import get_object_or_404
from animals import serializers
from animals.models import Animal
from animals.serializers import AnimalSerializer

# Create your views here.


class AnimalViews(APIView):
    def get(self, request: Request) -> Response:
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many = True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = AnimalSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    
class AnimalChangeViews(APIView):
    def get(self, request: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id = animal_id)
        serializer = AnimalSerializer(animal)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id = animal_id)
        serializer = AnimalSerializer(animal, request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id = animal_id)
        animal.delete()

        return Response(status.HTTP_204_NO_CONTENT)
