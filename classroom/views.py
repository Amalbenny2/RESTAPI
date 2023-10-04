from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from classroom.serializer import roomserializer

from .models import room
from classroom.serializer import roomserializer
# Create your views here.
@api_view(['GET','POST'])
def room_view(request):
    if request.method=="GET":
        Room=room.objects.all()
        serializers=roomserializer(Room,many=True)
        return Response(serializers.data)
    elif request.method=="POST":
        serializer=roomserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def room_details(request,id):
    try:
        Room=room.objects.get(id=id)
    except  room.DOESNOTEXIST:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = roomserializer(Room)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = roomserializer(Room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Room.delete()
        return Response(status==status.HTTP_204_NO_CONTENT)

