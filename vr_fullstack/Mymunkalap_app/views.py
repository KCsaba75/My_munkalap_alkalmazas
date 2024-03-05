from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.template import loader
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Gepjarmu, Hibatipusok, Megrendelo, Munkalap
from .serializers import GepjarmuSerializer, HibatipusokSerializer, MegrendeloSerializer, MunkalapSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.shortcuts import render, redirect
# Gepjarmu nézetek

class GepjarmuListView(ListView):
    queryset = Gepjarmu.objects.all()
    serializer_class = GepjarmuSerializer
    template_name = 'gepjarmu_list.html'

    #--------------
class MegrendeloListWithGepjarmuView(APIView):
    def get(self, request, *args, **kwargs):
        megrendelok = Megrendelo.objects.all()
        serializer = MegrendeloSerializer(megrendelok, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    template_name = 'megrendelo_lista_gepjarmuvekkel.html'




def Megrendelesek(request):
    adatok = Megrendelo.objects.all().values()
    template = loader.get_template('proba.html')
    context = {
            'adatok': adatok,
    }
    return HttpResponse(template.render(context, request))  


@api_view(['GET', 'POST'])
def megrendelokHandler(request):
    if request.method == 'GET':
        # adja vissza a taskokat
        tasks = Megrendelo.objects.all().values()
        serialized = MegrendeloSerializer(tasks, many = True)
        return Response(serialized.data)

    if request.method == 'POST':
        # hozzon létre új taskot
        text = request.data['text']
        task = Megrendelo(text=text)
        task.save()
        serialized = MegrendeloSerializer(task, many=False)
        return Response(serialized.data)
