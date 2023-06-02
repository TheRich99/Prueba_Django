
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from .serializer import PersonaSerializer,TareaSerializer
from .filters import TareaFilter,PersonaFilter
from .models import Persona,Tarea

# Create your views here.
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filterset_class=PersonaFilter



class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_class = TareaFilter   
    