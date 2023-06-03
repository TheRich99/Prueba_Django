from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, TareaViewSet

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]