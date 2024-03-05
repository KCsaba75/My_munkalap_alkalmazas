from rest_framework.serializers import ModelSerializer
from .models import Gepjarmu, Megrendelo,Munkalap, Hibatipusok



class GepjarmuSerializer(ModelSerializer):
    class Meta:
        model = Gepjarmu
        fields = ['id','rendszam', 'gyartmany', 'tipus', 'gyartasi_ev', 'alvazszam']


class HibatipusokSerializer(ModelSerializer):
    class Meta:
        model = Hibatipusok
        fields = ['id','hiba']


class MegrendeloSerializer(ModelSerializer):
    class Meta:
        model = Megrendelo
        fields = ['id','gepjarmu_ID', 'nev', 'cim', 'email', 'telefon']


class MunkalapSerializer(ModelSerializer):
    class Meta:
        model = Munkalap
        fields = ['id','megrendelo_id', 'datum', 'utolsomodositas', 'munkalapstatus', 'munkalapszam', 'kmoraallas', 'uzemenyagszint', 'hibatipus_id', 'hibaleiras', 'varhatohatarido', 'elvegzettmunka', 'felhasznaltanyag']
