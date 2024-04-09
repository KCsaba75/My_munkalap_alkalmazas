
from rest_framework import serializers
from .models  import Munkalap, Megrendelo, Gepjarmu, Hibatipusok


class GepjarmuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gepjarmu
        fields = ['id', 'megrendelo_id', 'rendszam', 'gyartmany', 'tipus', 'gyartasi_ev', 'alvazszam']

class HibatipusokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hibatipusok
        fields = ['id', 'hiba']

class MegrendeloSerializer(serializers.ModelSerializer):
     class Meta:
        model = Megrendelo
        fields = ['id', 'nev', 'cim', 'email', 'telefon']



# ----Munkalap seriolizer

class MunkalapSerializer(serializers.ModelSerializer):
    munkalapstatus = serializers.CharField(source='get_munkalapstatus_display')
    uzemenyagszint = serializers.CharField(source='get_uzemenyagszint_display')
    megrendelo_id = MegrendeloSerializer()
    gepjarmu_id=GepjarmuSerializer()
    hibatipus_id= HibatipusokSerializer()
    class Meta:
        model = Munkalap
        fields = '__all__'

    def get_uzemenyagszint_display(self, obj):
        uzemenyagszint_choices = dict(Munkalap.UZEMENYAGSZINT_CHOICES)
        return uzemenyagszint_choices.get(obj.uzemenyagszint, obj.uzemenyagszint)

        