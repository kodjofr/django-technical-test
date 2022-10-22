from rest_framework import serializers
from core.models import Client, ComptesEspece, ImputationsEspeces


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ComptesEspeceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComptesEspece
        fields = '__all__'


class ImputationsEspecesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImputationsEspeces
        fields = '__all__'
