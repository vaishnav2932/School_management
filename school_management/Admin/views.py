from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import AllowAny
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from library.permissions import *

# office_staff get
class OfficeStaffGet(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self,request,pk=None):
     if pk:
        try:
            officestaff=Office_staff.objects.get(pk=pk)
            serializer =OfficeStaffSerializer(officestaff)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Office_staff.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
     else:
         officestaffs = Office_staff.objects.all()
         serializer = OfficeStaffSerializer(officestaffs,many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
# office_staff createview
class ofiicestaff_creationview(APIView):
    permission_classes=[IsAuthenticated,IsAdmin]

    def post(self,request):
        serializers = OfficeStaffSerializer(data=request.data, context={'request':request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# librarian get
class LibrarianGet(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def get(self,request,pk=None):
        if pk:
            try:
                librarian=Librarian.objects.get(pk=pk)
                serializer =LibrarianSerializer(librarian)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except Librarian.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            librarians = Librarian.objects.all()
            serializer = LibrarianSerializer(librarians,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)




    # librarian_createview
class librarian_createview(APIView):
        permission_classes=[IsAuthenticated,IsAdmin]


        def post(self,request):
            serializers = LibrarianSerializer(data=request.data, context={'request':request})
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # office_staff updateview
class officestaff_updateview(APIView):
    permission_classes=[IsAuthenticated,IsAdmin]

    def put(self,request,pk):
        try:
            office_ob = Office_staff.objects.get(pk=pk)
        except Office_staff.DoesNotExist:
            return Response({'error:user not exist'},status=status.HTTP_404_NOT_FOUND)
        
        serializers = OfficeStaffSerializer(office_ob, data=request.data,partial=True, context={'request':request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    # office_staff deleteview
    def delete(self,request,pk):
        try:
            office_ob = Office_staff.objects.get(pk=pk)
            office_ob.delete()
            return Response({'message':'user deleted'},status=status.HTTP_200_OK)
        except Office_staff.DoesNotExist:
            return Response({'error:user not exist'},status=status.HTTP_404_NOT_FOUND)

# librarian_updateview
class librarian_updateview(APIView):
    permission_classes=[IsAuthenticated,IsAdmin]

    def put(self,request,pk):
        try:
            librarian_obj = Librarian.objects.get(pk=pk)
        except Librarian.DoesNotExist:
            return Response({'error:user not exist'},status=status.HTTP_404_NOT_FOUND)
        
        serializers = LibrarianSerializer(librarian_obj, data=request.data,partial=True,context={'request':request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    # librarian_delete
    def delete(self,request,pk):
        try:
            librarian_ob = Librarian.objects.get(pk=pk)
            librarian_ob.delete()
            return Response({'message':'user deleted'},status=status.HTTP_200_OK)
        except Librarian.DoesNotExist:
            return Response({'error:user not exist'},status=status.HTTP_404_NOT_FOUND)

            #student_createview  
class Student_creation(APIView):
    permission_classes=[IsAuthenticated,IsAdmin]

    def post(self,request):
        serializers = StudentSerializer(data=request.data,context={'request':request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # student_updateview
class student_update(APIView):
    permission_classes=[IsAuthenticated,IsAdmin]

    def put(self,request,pk):
        try:
            student_obj = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'error:user not exist'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student_obj,data=request.data,partial=True,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # student_deleteview
    def delete(self,request,pk):
        try:
            student_obj = Student.objects.get(pk=pk)
            student_obj.delete()
            return Response({'message':'user deleted'},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'error:user not exist'},status=status.HTTP_404_NOT_FOUND)
        
        # student_detail view for admin and librarian
class student_details(APIView):
    permission_classes=[IsAuthenticated,IsAdminOrLibrarian]

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
            serializers=StudentSerializer(students,many = True)
            return Response(serializers.data,status=status.HTTP_200_OK)