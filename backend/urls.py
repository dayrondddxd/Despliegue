"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('productos/',views.productos, name='productos'),
    # path('vaciar/',views.vaciar, name='vaciar'),
    # path('ordenar/',views.ordenar, name='ordenar'),
    path('productos/add/',views.add_producto, name='add_producto'),   
    path('productos/<int:detalle_id>/',views.detalle, name='detalle_producto'),   
    path('productos/<int:detalle_id>/eliminar',views.eliminar, name='eliminar'),  
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    path('administracion/',views.administracion, name='administracion'),

    path('ordenes/',views.ordenes, name='ordenes'),
    path('ordenes/addorden/',views.add_orden, name='add_orden'),  
    path('ordenes/<int:detalleorden_id>/',views.detalleorden, name='detalle_orden'), 
    path('ordenes/<int:detalleorden_id>/eliminar',views.eliminarorden, name='eliminarorden'),

    path('admin/',views.signinToAdmin, name='signinToAdmin'), 
     
    ]


