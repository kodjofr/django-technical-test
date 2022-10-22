from django.urls import path
from . import views

urlpatterns = [

    # about clients management
    path('', views.ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/new', views.ClientCreateView.as_view(), name='client_new'),
    path('client/<int:pk>/edit', views.ClientUpdateView.as_view(), name='client_edit'),
    path('client/<int:pk>/delete', views.ClientDeleteView.as_view(), name='client_delete'),

    # about accounts management
    path('comptesespece/', views.ComptesEspeceListView.as_view(), name='comptesespece_list'),
    path('comptesespece/<int:pk>', views.ComptesEspeceDetailView.as_view(), name='comptesespece_detail'),
    path('comptesespece/new', views.ComptesEspeceCreateView.as_view(), name='comptesespece_new'),
    path('comptesespece/<int:pk>/edit', views.ComptesEspeceUpdateView.as_view(), name='comptesespece_edit'),
    path('comptesespece/<int:pk>/delete', views.ComptesEspeceDeleteView.as_view(), name='comptesespece_delete'),

    # about transactions management
    path('imputationespeces/', views.ImputationsEspecesListView.as_view(), name='imputationespeces_list'),
    path('imputationespeces/<int:pk>', views.ImputationsEspecesDetailView.as_view(), name='imputationespeces_detail'),
    path('imputationespeces/new', views.ImputationsEspecesCreateView.as_view(), name='imputationespeces_new'),
    path('imputationespeces/<int:pk>/edit', views.ImputationsEspecesUpdateView.as_view(), name='imputationespeces_edit'),
    path('imputationespeces/<int:pk>/delete', views.ImputationsEspecesDeleteView.as_view(), name='imputationespeces_delete'),
]


