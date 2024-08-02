from django.db import models
from django.utils import timezone
# Create your models here.

class Proovedor(models.Model):
     tipo = models.CharField(max_length=100)

     def __str__(self):
          return self.tipo

class Productos(models.Model):

     class PostObjects(models.Manager):
          def get_queryset(self):
               return super().get_queryset().filter(disponibilidad='disponible')
          
     disponible='dis'
     agotado='ago'
     options=[
          (disponible,'Disponible'),
          (agotado,'Agotado'), 
     ]
     nombre = models.CharField(max_length=100)
     precio = models.IntegerField()
     cantidad = models.IntegerField()
     proovedor = models.ForeignKey(Proovedor,on_delete=models.CASCADE)
     contacto = models.CharField(max_length=100)
     disponibilidad = models.CharField(max_length=100,choices=options,default='disponible')
     objects = models.Manager()
     PostObjects = PostObjects()

     def __str__(self):
          return self.nombre
 
class DetalleOrdenes(models.Model):
     grande='gran'
     mediana='med'
     pequena='peque'
     options=[
          (grande,'Grande'),
          (mediana,'Mediana'),
          (pequena,'Pequena'),
     ]
     tamano = models.CharField(max_length=100,choices=options,default='pequena')
          
     def __str__(self):
          return self.tamano

class Ordenes(models.Model):
     nombre = models.CharField(max_length=100)
     detalleordenes = models.OneToOneField(DetalleOrdenes, on_delete=models.CASCADE)
     folio = models.IntegerField()
     
     def __str__(self):
          return self.nombre

class Empleado(models.Model):
     nombre = models.CharField(max_length=100)
     direccion = models.CharField(max_length=100)

class Cliente(models.Model):
     nombre = models.CharField(max_length=100) 
     ci = models.IntegerField()
     pedidos = models.ManyToManyField(Empleado)
     