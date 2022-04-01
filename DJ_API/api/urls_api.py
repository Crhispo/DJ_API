from django.urls import path
from DJ_API.api.views import CompaniaView

urlpatterns = [
    path('compañias/', CompaniaView.as_view(), name='ListaCompanias'),
]
