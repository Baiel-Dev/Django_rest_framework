from django.forms import model_to_dict
from django.utils.autoreload import raise_last_exception
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})


    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
                return Response({"error":"Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Objects dose not exits"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"post": serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Delete not allowed"})



        return Response({"post": "delete post" +str(pk)})