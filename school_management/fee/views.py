from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from library.permissions import *
from .permissions import *

# fee control for admin and officestaff
class feecontrol_createview(APIView):
    permission_classes = [IsAuthenticated,IsAdminOrOfficeStaff]

    def post(self, request, *args, **kwargs):
       
            serializer = feecontrolSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
         feecontrol = Fee.objects.all()
         serializer = feecontrolSerializer(feecontrol,many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            fee_control = Fee.objects.get(pk=pk)
        except Fee.DoesNotExist:
             return Response({'error':'Fee history doesnot exist'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = feecontrolSerializer(fee_control,data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
         try:
              fee_control = Fee.objects.get(pk=pk)
         except Fee.DoesNotExist:
              return Response({'error':'Fee history doesnot exist'},status=status.HTTP_404_NOT_FOUND)
         fee_control.delete()
         return Response({'message':'Fee history deleted'},status=status.HTTP_200_OK)
         
     

    