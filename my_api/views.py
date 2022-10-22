
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from core.models import Client, ComptesEspece, ImputationsEspeces
from .serializers import ClientSerializer, ComptesEspeceSerializer, ImputationsEspecesSerializer



class ClientCreateApiView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ComptesEspeceCreateApiView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ComptesEspece.objects.all()
    serializer_class = ComptesEspeceSerializer


class ImputationsEspecesCreateApiView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ImputationsEspeces.objects.all()
    serializer_class = ImputationsEspecesSerializer


class ClientListApiView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ComptesEspeceListApiView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ComptesEspece.objects.all()
    serializer_class = ComptesEspeceSerializer


class ImputationsEspecesListApiView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ImputationsEspeces.objects.all()
    serializer_class = ImputationsEspecesSerializer



class ClientRetrieveApiView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ComptesEspeceRetrieveApiView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ComptesEspece.objects.all()
    serializer_class = ComptesEspeceSerializer


class ImputationsEspecesRetrieveApiView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ImputationsEspeces.objects.all()
    serializer_class = ImputationsEspecesSerializer


class ClientUpdateApiView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ComptesEspeceUpdateApiView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ComptesEspece.objects.all()
    serializer_class = ComptesEspeceSerializer


class ImputationsEspecesUpdateApiView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ImputationsEspeces.objects.all()
    serializer_class = ImputationsEspecesSerializer


class ClientDestroyApiView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ComptesEspeceDestroyApiView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ComptesEspece.objects.all()
    serializer_class = ComptesEspeceSerializer


class ImputationsEspecesDestroyApiView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ImputationsEspeces.objects.all()
    serializer_class = ImputationsEspecesSerializer
