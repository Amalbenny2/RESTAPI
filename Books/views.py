from django.shortcuts import render
from  .models import Author,Book
from Books.serializer import Authorserializer,Bookserializer
from rest_framework import generics


class Author_list(generics.ListCreateAPIView):
    queryset = Author. objects.all()
    serializer_class = Authorserializer

class Author_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserializer

class Book_list(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class Book_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
# Create your views here.
