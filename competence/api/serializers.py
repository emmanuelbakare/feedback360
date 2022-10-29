from rest_framework import serializers
from competence.models import Competence, Bundle 

class CompetenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competence 
        fields = ('id','name')

