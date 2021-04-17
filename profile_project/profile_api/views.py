from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class ApiView(APIView):


    def get(self,request):


        an_api=[
            'an api view gives most control over your logic.',
            'is mapped manually to URL',
            'uses HTTP methods as function put get delete update post'
            ]
        return Response({'massege':'Hello Api','an_api':an_api})