from django.shortcuts import render
from django.views.generic import ListView # puisque on va utiliser la pagination pour les differant page

# class List(ListView):
#     template_name='blog/index.html'

def index(request):
    return render(request,'blog/index.html')
    