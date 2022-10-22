from django.urls import path
from .views import (
    ClientListApiView, ComptesEspeceListApiView, ImputationsEspecesListApiView,
    ClientRetrieveApiView, ComptesEspeceRetrieveApiView, ImputationsEspecesRetrieveApiView,
    ClientUpdateApiView, ComptesEspeceUpdateApiView, ImputationsEspecesUpdateApiView,

)

urlpatterns = [

    path('client/', ClientListApiView.as_view(), name='client-list'),
    path('comptes_espece/', ComptesEspeceListApiView.as_view(), name='comptes_espece-list'),
    path('imputations_especes/', ImputationsEspecesListApiView.as_view(), name='imputations_especes-list'),

    path('client/<int:pk>/', ClientRetrieveApiView.as_view(), name='client-detail'),
    path('comptes_espece/<int:pk>/', ComptesEspeceRetrieveApiView.as_view(), name='comptes_espece-detail'),
    path('imputations_especes/<int:pk>/', ImputationsEspecesRetrieveApiView.as_view(), name='imputations_especes-detail'),

    path('client/<int:pk>/update/', ClientUpdateApiView.as_view(), name='client-update'),
    path('comptes_espece/<int:pk>/update/', ComptesEspeceUpdateApiView.as_view(), name='comptes_espece-update'),
    path('imputations_especes/<int:pk>/update/', ImputationsEspecesUpdateApiView.as_view(), name='imputations_especes-update'),


]

