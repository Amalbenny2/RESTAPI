from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from studentapp.forms import Studentsform
from studentapp.models import Students
from studentapp.serializer import Studentsserializer



@api_view(['GET','POST'])
def student_list(request):
    if request.method =='GET':
        student =Students.objects.all()
        serializer = Studentsserializer(student,many=True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer= Studentsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)


    if request.method=='GET':
        serializer=Studentsserializer(student)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer= Studentsserializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)