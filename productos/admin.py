from django.contrib import admin
from .models import Productos, Proovedor,DetalleOrdenes,Ordenes,Empleado,Cliente
# Register your models here.

admin.site.register(Productos)
admin.site.register( Proovedor)
admin.site.register(DetalleOrdenes)
admin.site.register( Ordenes)
admin.site.register( Empleado)
admin.site.register( Cliente)

