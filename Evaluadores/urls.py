from django.urls import path
from . import views

urlpatterns = [
    path('evaluadores', views.post_evaluadores, name='evaluadores'),
    path('add_evaluador', views.add_evaluador, name='add_evaluador')
]