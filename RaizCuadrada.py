
"""
author: Alejandra Jiménez Soto
date: 10/21/2022

"""

a=2
b=0
delta = 1
while abs(b**2-a)>0.0000000000001:
    print("Probando con: ",b,"Incremento de: " ,delta)
    b = b + delta
    if (b**2)>a:
        b = b-delta
        delta = delta/10
print(b)