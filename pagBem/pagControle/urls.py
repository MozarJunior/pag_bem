from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    #Login e Cadastro
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('register', views.register, name='register'),
    #Estabelcimento
    path('estabelecimento/', views.estabelecimento_index, name="estabelecimento"),
    #Plano
    path('plano/create/', views.create_plano, name="create_plano"),
    path('plano/update/<str:pk>/', views.update_plano, name="update_plano"),
    path('plano/delete/<str:pk>/', views.delete_plano, name="delete_plano"),
    #Cliente
    path('cliente/', views.cliente_index, name="cliente"),
    path('cliente/estabelecimento/', views.cliente_estabelecimento, name="cliente_estabelecimento"),
    path('cliente/plano/', views.cliente_plano, name="plano_cliente"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]