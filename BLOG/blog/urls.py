from django.urls import path
from .views import *

urlpatterns = [
    path('',List.as_view(),name='home'),
    path('detail/<slug:slug>',DetailView,name='detailView')
]
