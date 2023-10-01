from rest_framework import serializers
from studentapp.models import Students

class Studentsserializer(serializers.ModelSerializer):
    class Meta:
        model =Students
        fields ='__all__'

