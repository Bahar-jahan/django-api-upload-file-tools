from rest_framework.views import APIView
from rest_framework import status
from apps.datastorege.models import FileUploadModel
from rest_framework.response import Response
from rest_framework import generics
from .serializer import *


# ------------------------------------------------------------------------
# create view API class  ----> adds file to API in CLI.PY :
class FileUploadCreateAPI(APIView):

    def post(self, request, *args, **kwargs):
        serializer = FileUploadCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------
# generic create view  API class  ----> add file to API by using building form :
class FileUploadListAPI(generics.ListCreateAPIView):
    queryset = FileUploadModel.objects.all()
    serializer_class = FileUploadCreateSerializer
