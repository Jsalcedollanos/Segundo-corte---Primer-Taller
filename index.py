# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 07:44:12 2021

@author: sistema
"""
# primer commit en la clase 1 segundo corte.
# Haga un algoritmo que determine que persona es mayor de edad
edad = int(input('Ingrese su edad: '))
if (edad >=18):
    print('Usted es mayor de edad!')
else:
    print('Usted es menor de edad!')

# =============================================================================
# . Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.
# =============================================================================
cant = int(input('Cantidad de camisas que desea comprar: '))
val = int(input('Ingrese valor de la camisa: '))
if (cant >= 3):
    res = int(val * cant)
    des = int(res * 0.3)
    total = int(res - des)
    print('Descuento del 30% es: ',des)
    print('El total a pagar es: ',total)
else:
    res = int(val * cant)
    des = int(res * 0.1)
    total = int(res - des)
    print('Descuento del 10% es: ',des)
    print('El total a pagar es: ',total)
    
# =============================================================================
# En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a descuento es 
# del 20%. Obtener cuanto dinero se le descuenta
# =============================================================================
azar = int(input('Escoja un numero del 1 al 100: '))
total = int(input('Valor de la compra: '))
if (azar < 74):
    promo = int(total * 0.15)
    pagoTotal = (total - promo)
    print('Descuento del 15%: ',promo)    
    print('Total a pagar: ',pagoTotal)

if (azar <= 100):
    promo = int(total * 0.2)
    pagoTotal = (total - promo)
    print('Descuento del 20%: ',promo)    
    print('Total a pagar: ',pagoTotal)