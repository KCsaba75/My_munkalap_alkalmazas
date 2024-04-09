# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Munkalap, Gepjarmu, Megrendelo, Hibatipusok
from .serializers import MunkalapSerializer, GepjarmuSerializer, MegrendeloSerializer, HibatipusokSerializer

# gépjármű nézetek
class OsszesGepjarmuJsonView(APIView):
    def get(self, request, *args, **kwargs):
        gepjarmuvek = Gepjarmu.objects.all()
        serializer = GepjarmuSerializer(gepjarmuvek, many=True)
        return Response(serializer.data)




# munkalap nézetek

class AktivMunkalapokJsonView(APIView):
    def get(self, request, *args, **kwargs):
        aktiv_munkalapok = Munkalap.objects.filter(munkalapstatus='enum_value_1')
        serializer = MunkalapSerializer(aktiv_munkalapok, many=True)
        return Response(serializer.data)
    
class InAktivMunkalapokJsonView(APIView):
    def get(self, request, *args, **kwargs):
        inaktiv_munkalapok = Munkalap.objects.filter(munkalapstatus='enum_value_2')
        serializer = MunkalapSerializer(inaktiv_munkalapok, many=True)
        return Response(serializer.data)



class OsszesMunkalapokJsonView(APIView):
    def get(self, request, *args, **kwargs):
        munkalapok = Munkalap.objects.all()
        serializer = MunkalapSerializer(munkalapok, many=True)
        return Response(serializer.data)
    
class UjMunkalapCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MunkalapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)