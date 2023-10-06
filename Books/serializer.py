from rest_framework import serializers
from Books.models import Author,Book


class Bookserializer(serializers.ModelSerializer):
   class Meta:
        model = Book
        fields = ('title','ratings','author')

class Authorserializer(serializers.ModelSerializer):
    book = Bookserializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields =('first_name','last_name','book')




