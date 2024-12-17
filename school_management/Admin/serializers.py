from rest_framework import serializers
from Accounts.models import *

# create Office staff
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OfficeStaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Office_staff
        fields = '__all__'

    def create(sellf,validate_data):
        user_data = validate_data.pop('user')
        user = User.objects.create(**user_data,is_officestaff=True)
        # admin =  sellf.context['request'].user
        office_staff = Office_staff.objects.create(user=user,**validate_data)

        return office_staff
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user',None)
        user = instance.user
        if user_data:
            for attr,value in user_data.items():
                setattr(user,attr,value)
            user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



    
    
class LibrarianSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Librarian
        fields = '__all__'

    def create(self,validate_data):
        user_data = validate_data.pop('user')
        user = User.objects.create(**user_data, is_librarian=True)
        librarian = Librarian.objects.create(user=user,**validate_data)
        return librarian
    
    def update(self, instance, validated_data):
      user_data = validated_data.pop('user', None)
      user = instance.user
      if user_data:
          for attr, value in user_data.items():
              setattr(user, attr, value)
          user.save()
      for attr, value in validated_data.items():
          setattr(instance, attr, value)
      instance.save()
      return instance


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data,is_student = True)
        student = Student.objects.create(user=user, **validated_data)
        return student
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        user = instance.user
        if user_data:
            for attr, value in user_data.items():
                setattr(user, attr, value)
                user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
           