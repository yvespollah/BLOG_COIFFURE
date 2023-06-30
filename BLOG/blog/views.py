from django.shortcuts import render
from django.views.generic import ListView # puisque on va utiliser la pagination pour les differant page
from .models import *


class List(ListView):
    template_name='blog/index.html'
    queryset=CreateBlog.objects.all() # on vien de tout recuperer dans la bd et metre dans la variable queryset qui est un tablea
    paginate_by = 3

    