from rest_framework import authentication
from nhyu.models import Sweer23
from .serializers import Sweer23Serializer
from rest_framework import viewsets

class Sweer23ViewSet(viewsets.ModelViewSet):
    serializer_class = Sweer23Serializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Sweer23.objects.all()