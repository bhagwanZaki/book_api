from rest_framework.decorators import permission_classes
from .models import book
from rest_framework import serializers, viewsets,permissions,status
from rest_framework.views import Response,APIView
from .serializers import bookSerializers
from rest_framework.generics import RetrieveAPIView

class latestBookApi(APIView):
    permissions_classes = [permissions.AllowAny]

    def get(self,request,format=None):
        bookList = book.objects.all()

        try:
            if len(bookList) > 5:
                data = bookList[len(bookList)-5:]
            else:
                data = bookList

            data.reverse()
            serializer = bookSerializers(data,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except:
            return Response([],status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class bookApi(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = bookSerializers

    def get_queryset(self):
        bookList = book.objects.all()

        if len(bookList) > 5:
            data = bookList[:len(bookList)-5]
        else:
            data = bookList

        data.reverse()
        return data




