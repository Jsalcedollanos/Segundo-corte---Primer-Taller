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
    
# =============================================================================
# Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que conssite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente.
# =============================================================================
monto = int(input('Ingresa el monto: '))
if (monto < 50000):
    cuota = (monto * 0.03)
    print('Couta a pagar del 3%: ',cuota)
if (monto >= 50000):
    cuota = (monto * 0.02)
    print('Couta a pagar del 2%: ',cuota)
    
# =============================================================================
# Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.
# =============================================================================
medida = int(input('Ingrese la medida: en puntos de la semana: '))
salario = int(input('Ingrese salario: '))
promedio = (medida / 5)
if (promedio > 170):
    multa = salario * 0.5
    print('Se para la producion por 1 semana!')
    print('Total de la multa del 50% es: ',multa)
if (promedio <= 170):  
    print('EXCELENTE!! no tiene multa ni sancion')

# =============================================================================
# Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad 
# del incremento del valor del terreno. Ayúdale a esta pesona a determinar 
# si debe o no comprar el automóvil.
# =============================================================================
valor = int(input('Ingrese valor del auto: '))
desva = int(valor / 36)
valori = int(valor * 0.3)
mitad = int(valori / 2) 
print('Valor de la valoricacion: ',valori)
print('Valor de la desvaloricacion: ',desva)
print('Mitad de la valoricacion',mitad)
if (desva <= mitad):
    print('Compra carro!')
else:
    print('No compres carro!')
    
# =============================================================================
# En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que
# compre. Si las computadoras son menos de cinco se les dará un 10%
# de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco pero menos de diez se le
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
# precio de cada computadora es de $11.000.
# =============================================================================
cantidad = int(input('Ingrese la cantidad de computadores: '))
valor = int(input('Ingrese el valor a pagar: '))
if (cantidad < 5):
    desc = int(valor * 0.1)
    valorTotal = int(valor - desc)
    print('Total a pagar con descuento del 10% es: ',valorTotal)
if (cantidad >= 5 and cantidad < 10):
    desc = int(valor * 0.2)
    valorTotal = int(valor - desc)
    print('Total a pagar con descuento del 20% es: ',valorTotal)
if (cantidad >= 10):
    desc = int(valor * 0.4)
    valorTotal = int(valor - desc)
    print('Total a pagar con descuento del 40% es: ',valorTotal)

# =============================================================================
# Un proveedor de estéreos ofrece un descuento del 10% sobre el
# precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
# independientemente de esto, ofrece un 5% de descuento si la marca
# es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
# cualquiera por la compra de su aparato. IVA es del 16%.
# =============================================================================
valor = int(input('Ingrese valor del producto: '))
marca = str(input('la marca es NOSY (si) (no)'))

if (valor >= 2000 and marca == 'si'):
    bono = int(valor * 0.05)
    desc = int(valor * 0.1)
    iva = int(valor * 0.16)
    descuentoTotal = int(bono + desc)
    pagoTotal = int(valor + iva - descuentoTotal)
    print('recibe descuento del 5% y es de: ',bono)
    print('Recibes un descuento del 10% y es de: ',desc)
    print('Iva: ',iva)
    print('Total a pagar es: ',pagoTotal)

if (valor >= 2000 and marca == 'no'):
    desc = int(valor * 0.1)
    iva = int(valor * 0.16)
    pagoTotal = int(valor + iva - desc)
    print('Recibes un descuento del 10% y es de: ',desc)
    print('Iva: ',iva)
    print('Total a pagar es: ',pagoTotal)
    
if (valor < 2000 and marca == 'si'):
    bono = int(valor * 0.05)
    desc = int(valor * 0.1)
    iva = int(valor * 0.16)
    descuentoTotal = int(bono + desc)
    pagoTotal = int(valor + iva - descuentoTotal)
    print('recibe descuento del 5% y es de: ',bono)
    print('Recibes un descuento del 10% y es de: ',desc)
    print('Iva: ',iva)
    print('Total a pagar es: ',pagoTotal)
    
if (valor < 2000 and marca == 'no'):
    desc = int(valor * 0.1)
    iva = int(valor * 0.16)
    pagoTotal = int(valor + iva - desc)
    print('Recibes un descuento del 10% y es de: ',desc)
    print('Iva: ',iva)
    print('Total a pagar es: ',pagoTotal)