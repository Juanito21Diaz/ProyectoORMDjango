from django.shortcuts import render,HttpResponse
from appORM.models import *
from django.http import JsonResponse
from django.db.models import Q,Sum, Max, Count, Avg

# Create your views here.
#consultas a realizar
#1. Cantidad de productos vendidos por Categoria
#2. Valor total de venta por producto
#3. Valor total de Venta por Categoria
#4. Promedio de Ventas por mes
#5. Máximo valor de una venta
#6. Minimo valor de una venta
#7. Cantidad mayor de un producto vendido


def graficaGOOGLE(request):
    return render(request,"graficaGOOGLE.html")

def grafica1GOOGLE(request):
    ventasProducto = DetalleVenta.objects.values('detProducto').\
        annotate(TotalVentaProducto=Sum('detValorDetalle'))
        
    listaDatos = []
    listaDatos.append(['Producto','ValorVenta'])
    
    for ventaProducto in ventasProducto: #entra el producto
        produto= Producto.objects.get(pk=ventaProducto['detProducto']).proNombre
        valorVenta = ventaProducto['TotalVentaProducto']
        listaDatos.append([produto, valorVenta]) #agrega el producto, manda el nombre y el valor
        
    retorno = {'datos':listaDatos}
    return JsonResponse(retorno)