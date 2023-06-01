from rest_framework import serializers
from nhyu.models import Sweer23

class Sweer23Serializer(serializers.ModelSerializer):

    class Meta:
        model = Sweer23
        fields = "__all__"