from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import *
# Create your views here.

class HomePageView(ListView):
    model = Crypto
    template_name = 'index.html'
    context_object_name = 'cryptos'