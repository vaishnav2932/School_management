from rest_framework import serializers
from Accounts.models import *

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryTransaction
        fields ='__all__'