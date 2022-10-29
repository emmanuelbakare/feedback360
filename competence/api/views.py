from rest_framework import generics 
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.decorators import action
from competence.models import Competence, Bundle
from competence.api.serializers import CompetenceSerializer
from quality.api.serializers import QualitySerializer
from quality.models import Quality


# class CompetenceListCreate(generics.ListCreateAPIView):
#     queryset= Competence.objects.all() 

class CompetenceViewset(viewsets.ModelViewSet):
    queryset=Competence.objects.all()
    serializer_class= CompetenceSerializer


    @action(detail=True)
    def qualities(self, request, pk=None):

        if pk:
            try:
                qualities=Quality.objects.filter(competence=pk)
            except:
                return Response({"error": "Error getting data, id may not exist"})
            serialized=QualitySerializer(qualities, many=True)
            return Response(serialized.data)
        return Response({})

