from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Accounts.models import *
from .serializers import *
from Admin.permissions import *
from rest_framework.permissions import IsAuthenticated
from .permissions import*

# library_transaction creationview for admin
class Librarycreate(APIView):
    permission_classes =[IsAuthenticated,IsAdmin]

    def post(self,request):
        serializers = LibrarySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Library created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

# library_historyst view for admin and librarian
class LibraryHistory(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrLibrarian]

    def get(self, request, *args, **kwargs):
        library_history = LibraryTransaction.objects.all()
        serializer = LibrarySerializer(library_history, many=True)
        return Response(serializer.data)
    
    # library_historylist and update view for admin
class LibraryUpdate(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request, pk):
        try:
            transaction = LibraryTransaction.objects.get(pk=pk)
        except LibraryTransaction.DoesNotExist:
            return Response({'error': 'Library transaction not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = LibrarySerializer(transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request,pk):
        try:
            librari_transactions = LibraryTransaction.objects.get(pk=pk)
        except LibraryTransaction.DoesNotExist:
            return Response({'error':'Librari history not exist'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = LibrarySerializer(librari_transactions,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # library_history deleteview admin
class library_delete(APIView):
    permission_classes = [IsAdmin]

    def delete(self,request,pk):
        try:
            library_history = LibraryTransaction.objects.get(pk=pk)
        except LibraryTransaction.DoesNotExist:
            return Response({'error':'Library transaction not found'},status=status.HTTP_404_NOT_FOUND)
        library_history.delete()
        return Response({'message':'Library transaction deleted'},status=status.HTTP_200_OK)
                        


