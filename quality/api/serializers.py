from rest_framework import serializers 
from quality.models import Quality


class QualitySerializer(serializers.ModelSerializer):

    class Meta:
        model= Quality 
        fields  = "__all__"    