from django_filters import rest_framework as filters
import django_filters
from .models import Tarea,Persona

from django.db.models import CharField
from django.db.models.functions import Cast
from django.db.models import Value


class TareaFilter(filters.FilterSet):
    tipo_documento = filters.CharFilter(method='filter_tipo_documento')

    def filter_tipo_documento(self, queryset, name, value):
        return queryset.annotate(persona_documento=Cast('persona__documento', CharField())).filter(persona_documento__icontains=value)


    class Meta:
        model = Tarea
        fields = {
            'titulo': ['exact', 'icontains'],
            'fecha_limite': ['exact', 'gte', 'lte'],
            'persona':['exact'],
            
        }


""" class TareaFilter(filters.FilterSet):
    tipo_documento = filters.CharFilter(method='filter_tipo_documento')

    def filter_tipo_documento(self, queryset, name, value):
        return queryset.annotate(persona_documento=Cast('persona__documento', CharField())).filter(persona_documento__icontains=value)

    class Meta:
        model = Tarea
        fields = ['tipo_documento'] """

        

#?fecha_limite__gte=##-##-##&fecha_limite__lte=###-##-##
class PersonaFilter(filters.FilterSet):
    
    class Meta:
        model = Persona
        fields = {
            'documento':['exact', 'icontains'],
        }

