from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Sensor, TemperaturaData, UmidadeData, LuminosidadeData, ContadorData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}} # Código foi passado até aqui

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'  

class TemperaturaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaData
        fields = '__all__'

class UmidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmidadeData
        fields = '__all__'

class LuminosidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuminosidadeData
        fields = '__all__'
    
class ContadorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContadorData
        fields = '__all__'
    
    