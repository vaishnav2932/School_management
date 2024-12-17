from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Accounts.models import *
from .serializers import *
from .permissions import IsOfficeStaff
from rest_framework.permissions import IsAuthenticated

# student deatails get for office_staff
class StudentView(APIView):
    permission_classes = [IsAuthenticated,IsOfficeStaff]

    def get(self,request,id=None):
        if id:
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'error':'student not exist'},status=status.HTTP_404_NOT_FOUND)
        else:
                students = Student.objects.all()
                serializer = StudentSerializer(students, many=True)
                return Response(serializer.data)
        
        # library history get for office_staff
class libraryhistory(APIView):
     permission_classes  =[IsAuthenticated,IsOfficeStaff]

     def get(self,request,id=None):
        if id:
          try:
               library_history = LibraryTransaction.objects.get(id=id)   
               serializer =  libraryserializer(library_history)
               return Response(serializer.data,status=status.HTTP_200_OK)
          except LibraryTransaction.DoesNotExist:
               return Response({'error':'library history not exist'},status=status.HTTP_404_NOT_FOUND)
        else:
            Libraryhistory = LibraryTransaction.objects.all()
            serializer=libraryserializer(Libraryhistory,many=True)
            return Response(serializer.data)