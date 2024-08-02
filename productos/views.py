from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .forms import ProductoForm
from .forms2 import OrdenesForm
from .models import Productos,Ordenes
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

def signinToAdmin(request):
     user = authenticate(request, username=request.POST['betsy'], password=request.POST['betsy'])
     if user is not None:
          login(request,user)
          return HttpResponseRedirect('/admin/')

def home(request):
     return render(request,'home.html',)

def signup(request):
     if request.method =='GET':
         return render(request,'signup.html',{
          'form':UserCreationForm
     })
     else:
          if request.POST['password1']==request.POST['password2']:
               try:
                              # registrar User
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request,user)
                    return redirect('productos')
               except IntegrityError:
                     return render(request,'signup.html',{
               'form':UserCreationForm,"error":'Usuario ya existe'
          })
          return render(request,'signup.html',{
          'form':UserCreationForm,"error":'Contraseña no coiciden'
     })

@login_required
def productos(request):
     # productos = Productos.objects.all()
     # productos = Productos.objects.filter( disponibilidad = Productos.disponible)
     if request.user.username =='ddd':
          productos = Productos.objects.all()
          return render(request,'productos.html',{'productos':productos})
     # if request.user.username =='betsy':
     #      ordenes = Ordenes.objects.all()
     #      return render(request,'ordenes.html',{'ordenes':ordenes})
     else:
          productos = Productos.objects.filter( disponibilidad = Productos.disponible)
          return render(request,'productos.html',{'productos':productos})     
     
@login_required
def ordenes(request): 
     # if request.user.username =='betsy':
          ordenes = Ordenes.objects.all()
          return render(request,'ordenes.html',{'ordenes':ordenes})
     
def administracion(request):
     return render(request,'administracion.html',)

def add_producto(request):
     if request.method == 'GET':
          return render(request, 'add.html',{'form': ProductoForm})
     else:
          try:
               form = ProductoForm(request.POST) 
               nuevo_producto = form.save(commit=False)
               nuevo_producto.user = request.user
               nuevo_producto.save()
               return redirect('productos')
          except ValueError:
               return render(request, 'add.html', {'form': ProductoForm, 'error': 'Provee datos validos'}) 

@login_required
def add_orden(request):
     if request.method == 'GET':
          return render(request, 'addordenes.html',{'form': OrdenesForm})
     else:
          try:
               form = OrdenesForm(request.POST) 
               nueva_orden = form.save(commit=False)
               nueva_orden.user = request.user
               nueva_orden.save()
               return redirect('ordenes')
          except ValueError:
               return render(request, 'addordenes.html', {'form':  OrdenesForm, 'error': 'Provee datos validos'}) 

@login_required
def detalle(request, detalle_id):
     if request.method =='GET':
          # producto=Productos.object.all()
          # task = Task.objects.get(pk=task_id)
          producto = get_object_or_404(Productos,pk=detalle_id)
                                   #     user=request.user)
          form = ProductoForm(instance=producto)
          return render(request, 'detalle.html', {'producto': producto, 'form':form})
     else:
          try:
               producto = get_object_or_404(Productos,pk=detalle_id, )
               # user=request.user
               form = ProductoForm(request.POST, instance=producto)
               form.save()
               return redirect('productos')
          except ValueError:
               return render(request, 'detalle.html', {'producto': producto, 'form':form, 'error':"error modificando producto"})

@login_required
def detalleorden(request, detalleorden_id):
     if request.method =='GET':
          orden = get_object_or_404(Ordenes,pk=detalleorden_id)
          form = OrdenesForm(instance=orden)
          return render(request, 'detalleorden.html', {'orden': orden, 'form':form})
     else:
          try:
               orden = get_object_or_404(Ordenes,pk=detalleorden_id,)
               form = OrdenesForm(request.POST, instance=orden)
               form.save()
               return redirect('ordenes')
          except ValueError:
               return render(request, 'detalleorden.html', {'orden': orden, 'form':form, 'error':"error modificando orden"})


# def vaciar(request):
#       producto=get_object_or_404(Productos.object.get.all() )
#       if request.method=="POST":
#           producto.delete()
#           return redirect('productos',{'producto',producto})
      
# def ordenar(request):
#      productos=Productos.objects.order_by(precio)
#      if request.method=="POST":
#           return render(request,'productos.html',{'productos':productos})


@login_required
def eliminar(request,detalle_id):
     producto= get_object_or_404(Productos,pk=detalle_id)
     if request.method=="POST":
          producto.delete()
          return redirect('productos')
     
@login_required
def eliminarorden(request,detalleorden_id):
     ordenes= get_object_or_404(Ordenes,pk=detalleorden_id)
     if request.method=="POST":
          ordenes.delete()
          return redirect('ordenes')

def signout(request):
     logout(request)
     return redirect('home')

def signin(request):
     if request.method =='GET':
          return render(request, 'signin.html',{
            'form':AuthenticationForm
      })
     else:
          user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
          if user is None:
              return render(request, 'signin.html',{
            'form':AuthenticationForm, 'error':'usuario incorrecto'
      })  
          else:
               login(request,user)
               return redirect('productos')

def signin(request):
     if request.method =='GET':
          return render(request, 'signin.html',{
            'form':AuthenticationForm
      })
     else:
          user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
          if user is None:
              return render(request, 'signin.html',{
            'form':AuthenticationForm, 'error':'usuario incorrecto'
      })  
          else:
               login(request,user)
               return redirect('productos')








