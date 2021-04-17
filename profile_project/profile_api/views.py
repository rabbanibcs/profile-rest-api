from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import HelloSerializer
from rest_framework import status



class ApiView(APIView):

    serializer_class=HelloSerializer
    def get(self,request,format=None):


        an_api=[
            'an api view gives most control over your logic.',
            'is mapped manually to URL',
            'uses HTTP methods as function put get delete update post'
            ]
        return Response({'massege':'Hello Api','an_api':an_api})

    def post(self, request):

        serializer=HelloSerializer(data=request.data)
        if serializer.is_valid():
            # name=serializer.data.get('name')
            name=serializer.data['name']
            massage="Hello {}".format(name)
            return Response({'massage':massage})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        return Response({"method":"put"})
    def patch(self,request,pk=None):
        return Response({"method":"patch"})

    def delete(self,request,pk=None):
        return Response({"method":"delete"})

      
