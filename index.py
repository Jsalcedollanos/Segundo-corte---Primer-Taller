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
    