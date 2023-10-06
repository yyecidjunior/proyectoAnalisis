from django.db import models



class Cliente(models.Model):
    Nombre = models.CharField(max_length=100)
    Gmail = models.EmailField() 
    Celular = models.CharField(max_length=12) 
    Direccion = models.CharField(max_length=255)  


    