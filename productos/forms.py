# from django.forms import ModelForm
from django import forms
from .models import Productos,Ordenes

class ProductoForm(forms.ModelForm):
     class Meta:
          model = Productos
          fields = ['nombre', 'precio', 'cantidad','proovedor','contacto','disponibilidad',]
          widgets={
               'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el nombre'}),
               'precio':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el precio'}),
               'cantidad':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba la cantidad'}),
               'proovedor':forms.Select(attrs={'class':'form-control'}),
               'contacto':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el nombre'}),
               
               'disponibilidad':forms.Select(attrs={'class':'form-control'}),
          }

# class OrdenesForm(forms.ModelForm):
#      class Meta:
#           model = Ordenes
#           fields = ['nombre','detalleordenes','folio']
#           widgets={
#                'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el nombre'}),
#                'detalleordenes':forms.Select(attrs={'class':'form-control'}),
#                'folio':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el nombre'}),
               
#           }
