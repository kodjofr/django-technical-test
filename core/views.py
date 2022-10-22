from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client, ComptesEspece, ImputationsEspeces
from django.urls import reverse_lazy


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'client_list'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client_detail'


class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ['id_personne', 'id_classe', 'id_naturel_it', 'id_pays', 'nature_client', 'etat', 'id_categorie_avoir',
              'raison_sociale', 'matricule']
    success_url = reverse_lazy('client_list')


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client_edit.html'
    fields = ['id_personne', 'id_classe', 'id_naturel_it', 'id_pays', 'nature_client', 'etat', 'id_categorie_avoir',
              'raison_sociale', 'matricule']
    success_url = reverse_lazy('client_list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    context_object_name = 'client'
    success_url = reverse_lazy('client_list')


class ComptesEspeceListView(ListView):
    model = ComptesEspece
    template_name = 'comptesespece_list.html'
    context_object_name = 'comptesespece_list'


class ComptesEspeceDetailView(DetailView):
    model = ComptesEspece
    template_name = 'comptesespece_detail.html'
    context_object_name = 'comptesespece_detail'


class ComptesEspeceCreateView(CreateView):
    model = ComptesEspece
    template_name = 'comptesespece_new.html'
    fields = ['id_compte', 'id_client', 'id_depositaire', 'date_creation', 'web', 'etat']
    success_url = reverse_lazy('comptesespece_list')


class ComptesEspeceUpdateView(UpdateView):
    model = ComptesEspece
    template_name = 'comptesespece_edit.html'
    fields = ['id_compte', 'id_client', 'id_depositaire', 'date_creation', 'web', 'etat']
    success_url = reverse_lazy('comptesespece_list')


class ComptesEspeceDeleteView(DeleteView):
    model = ComptesEspece
    template_name = 'comptesespece_delete.html'
    context_object_name = 'comptesespece'
    success_url = reverse_lazy('comptesespece_list')


class ImputationsEspecesListView(ListView):
    model = ImputationsEspeces
    template_name = 'imputationespeces_list.html'
    context_object_name = 'imputationespeces_list'


class ImputationsEspecesDetailView(DetailView):
    model = ImputationsEspeces
    template_name = 'imputationespeces_detail.html'
    context_object_name = 'imputationespeces_detail'


class ImputationsEspecesCreateView(CreateView):
    model = ImputationsEspeces
    template_name = 'imputationespeces_new.html'
    fields = '__all__'
    success_url = reverse_lazy('imputationespeces_list')


class ImputationsEspecesUpdateView(UpdateView):
    model = ImputationsEspeces
    template_name = 'imputationespeces_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('imputationespeces_list')


class ImputationsEspecesDeleteView(DeleteView):
    model = ImputationsEspeces
    template_name = 'imputationespeces_delete.html'
    context_object_name = 'imputationespeces'
    success_url = reverse_lazy('imputationespeces_list')
