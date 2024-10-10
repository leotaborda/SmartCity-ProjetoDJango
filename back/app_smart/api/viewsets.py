from django.contrib.auth.models import User
from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from app_smart.api import serializers # app_smart é o app criado.
from rest_framework.response import Response
from ..models import Sensor, TemperaturaData, UmidadeData, LuminosidadeData, ContadorData
from rest_framework import viewsets
from app_smart.api.filters import SensorFilter, TemperaturaDataFilter
from django_filters.rest_framework import DjangoFilterBackend



class CreateUserAPIViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # Código foi passado até aqui
    
    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SensorFilter

class TemperaturaDataViewSet(viewsets.ModelViewSet):
    queryset = TemperaturaData.objects.all()
    serializer_class = serializers.TemperaturaDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TemperaturaDataFilter

class UmidadeDataViewSet(viewsets.ModelViewSet):
    queryset = UmidadeData.objects.all()
    serializer_class = serializers.UmidadeDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class LuminosidadeDataViewSet(viewsets.ModelViewSet):
    queryset = LuminosidadeData.objects.all()
    serializer_class = serializers.LuminosidadeDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContadorDataViewSet(viewsets.ModelViewSet):
    queryset = ContadorData.objects.all()
    serializer_class = serializers.ContadorDataSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserAPIViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = serializers.UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = serializers.UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        