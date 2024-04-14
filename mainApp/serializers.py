from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Qoshiqchi, Albom, Qoshiq


class QoshiqchiSerializer(ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'


class AlbomSerializer(ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'


class QoshiqSerializer(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_audio(self, qiymat):
        if not str(qiymat).endswith('.mp3'):
            raise serializers.ValidationError("Loyiha faqat .mp3 fayllar bilash ishlashi mumkin!")
        return qiymat

    def validate_davomiylik(self, qiymat):
        if str(qiymat) > "00:06:00":
            raise serializers.ValidationError("Qo'shiqning davomiyligi 6 daqiqadan oshmasin!")
        return qiymat
