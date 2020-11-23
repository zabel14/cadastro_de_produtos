import include as include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto_cadastrar/', views.produto_cadastrar, name='produto_cadastrar'),
    path('produto_cadastrar_sucesso/', views.produto_cadastrar_sucesso, name='produto_cadastrar_sucesso'),
    path('produto_listar/', views.produto_listar, name='produto_listar'),
    path('produto_remover/<int:pk>', views.produto_remover, name='produto_remover'),
    path('produto_editar/<int:pk>', views.produto_editar, name='produto_editar'),
    path('produto_editar_sucesso/', views.produto_editar_sucesso, name='produto_editar_sucesso')
]
