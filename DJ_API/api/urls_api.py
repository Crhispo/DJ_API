from django.urls import path
from DJ_API.api.views import CompaniaView

urlpatterns = [
    path('compañias/', CompaniaView.as_view(), name='ListaCompanias'),
    path('compañias/<int:id>', CompaniaView.as_view(), name='ListarCompania'),
]
