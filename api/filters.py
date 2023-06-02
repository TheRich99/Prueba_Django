from django_filters import rest_framework as filters
import django_filters
from .models import Tarea,Persona

class TareaFilter(filters.FilterSet):

    class Meta:
        model = Tarea
        fields = {
            'titulo': ['exact', 'icontains'],
            'fecha_limite': ['exact', 'gte', 'lte'],
            'persona':['exact'],
            
        }



#?fecha_limite__gte=##-##-##&fecha_limite__lte=###-##-##
class PersonaFilter(filters.FilterSet):
    
    class Meta:
        model = Persona
        fields = {
            'documento':['exact', 'icontains'],
        }

