from django.shortcuts import render

# Create your views here.
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'item_list_template.html'
    
class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'item_detail_template.html'
    
class ItemCreateView(CreateView):
    model = Item
    template_name = 'item_create_template.html'
    fields = ['name', 'price', 'user','description']
    success_url = reverse_lazy('item_list_url')