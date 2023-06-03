from django_filters import rest_framework as filters
import django_filters
from .models import Tarea,Persona

from django.db.models import CharField
from django.db.models.functions import Cast
from django.db.models import Value


""" class TareaFilter(filters.FilterSet):
    fecha_limite_min = filters.DateFilter(field_name='fecha_limite', lookup_expr='gte')
    fecha_limite_max = filters.DateFilter(field_name='fecha_limite', lookup_expr='lte')


    class Meta:
        model = Tarea
        fields = ['fecha_limite_min', 'fecha_limite_max','persona']
 """

class TareaFilter(filters.FilterSet):
    class Meta:
        model = Tarea
        fields = {
            'titulo': ['exact', 'icontains'],
            'descripcion': ['exact', 'icontains'],
            'fecha_limite': ['exact', 'gte', 'lte'],
        }
#?fecha_limite__gte=##-##-##&fecha_limite__lte=###-##-##
class PersonaFilter(filters.FilterSet):
    
    class Meta:
        model = Persona
        fields = {
            'documento':['exact', 'icontains'],
        }

