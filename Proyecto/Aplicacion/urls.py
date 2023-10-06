from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.exit, name='exit'),
    path('register/', views.register, name='register'),
    path('registrarCliente/', views.registrarCliente, name='registrarCliente'),
    path('cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('editarInfo/<int:cliente_id>/', views.editarInfo, name='editarInfo'),
    path('edicionCliente/<int:cliente_id>/', views.edicionCliente, name='edicionCliente'),
    

]  
