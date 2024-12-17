from rest_framework import serializers
from Accounts.models import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'

class libraryserializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryTransaction
        fields = '__all__'        