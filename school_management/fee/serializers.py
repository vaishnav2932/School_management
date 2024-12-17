from rest_framework import serializers
from Accounts.models import *

class feecontrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields ='__all__'