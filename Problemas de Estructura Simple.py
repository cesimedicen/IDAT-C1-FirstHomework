
# PROBLEMA 1
# Calcular el área de un trapecio
print("Ingrese la base menor: ")
Bm=int(input())
print("Ingrese la base mayor: ")
BM=int(input())
print("Ingrese la altura: ")
H=int(input())
A= ((Bm+BM)/2)*H
print("El area es")
print(A)

# PROBLEMA 2
# Invertir números
N1= input("Ingrese el numero a invertir:")
N1=N1[::-1]
print(N1)   

#PROBLEMA 3
print("Ingrese su sueldo basico:")
SB=int(input())
B= 0.2*SB
D= 0.1*SB
SN= SB+B-D
print("Tu sueldo neto es")
print(SN)

#PROBLEMA 4
# Hallar volumen del cilindro
print("Ingrese el radio")
R=int(input())
print("Ingrese la altura")
H=int(input())
PI=3.1416
A= PI*R**2
V=A*H
print("El volumen del cilindro es")
print(V)

#PROBLEMA 5
print("Ingrese el numero de palabras")
NP=int(input())
print("Ingrese el tamaño en milimetro")
M=int(input())
print("Ingrese el numero de colores")
NC=int(input())
PP=1
PM=1.5
PC=3
TOTAL= (NP*PP)+(M*PM)+(NC*PC)
print("El costo total a pagar es")
print(TOTAL)

#PROBLEMA 6
print("Ingrese un número")
N=int(input())
N1= 0.1*N
N2= 0.2*N
N3= 0.3*N
SUMA= N1+N2+N3
print("el 10% es:")
print(N1)
print("el 20% es:")
print(N2)
print("el 30% es:")
print(N3)
print("La suma es:")
print(SUMA)

#PROBLEMA 7





#PROBLEMA 8
print("Ingrese el grado de Celsius")
C=int(input())
F=9*C/5+23
print("La temperatura en grados Fahrenheit es:",F)

#PROBLEMA 9
print("Ingrese su sueldo base")
SB=int(input())
print("Ingrese su cantidad de hijos")
H=int(input())
NH= H*80
SN= SB+NH
print("Su bonificación familiar es:",NH)
print("Su sueldo neto es:",SN)

#PROBLEMA 10

print("Ingrese el valor de A :")
A=int(input())
print("Ingrese el valor de Vo :")
Vo=int(input())
print("Ingrese el valor de T :")
T=int(input())
D= (Vo*T)+-1/2*(A*T**2)
print("La distancia recorrida es:")
print(D)

#PROBLEMA 11
print("Ingrese su saldo inicial :")
Si=int(input())
Interes=Si*2.5/100*6
SF=Si+Interes
print("Su saldo final despues de 6 meses es:")
print(SF)

#PROBLEMA 12
print("Ingrese el n° de horas dictadas al mes:")
NH=int(input())
PM=20*NH
print("El pago sin descuento es:",PM)
D=0.05*PM
PN=PM-D
print("El descuento es:",D)
print("El pago neto es:",PN)

#PROBLEMA 13
print("Ingrese el numero de fotos que desea revelar:")
NF=int(input())
P=0.5
IGV=0.18*P
TOTAL=NF*P+IGV
print("El total a pagar seria:",TOTAL)

#PROBLEMA 14
print("Ingrese los años laborados:")
A=int(input())
# PrimerAño= 100(no se como condicionar esto)
Año= 120
Bono= Año*A
print("Su bono total es:", Bono)

#PROBLEMA 15
print("Ingrese el valor de Radio")
R=int(input())
print("Ingrese la altura")
H=int(input())
PI= 3.14
V=(PI*(R**2)*H)/3
print("El volumen del cono es:", V)

#PROBLEMA 16
print("Ingrese el valor de Radio")
R=int(input())
PI=3.14
V=(4/3)*PI*R**3
print("El volumen de la esfera es:", V)

#PROBLEMA 17
print("Ingrese la cantidad de Kilometros recorridos")
Km=int(input())
print("Ingrese el tiempo en minutos")
Min=int(input())
TOTAL=(Km*5)+(Min*2)
print("El costo total a pagar es:", TOTAL)

#PROBLEMA 18
print("Ingrese el valor de A :")
A=int(input())

print("Ingrese el valor de B :")
B=int(input())
print("Ingrese el valor de Y :")
Y=int(input())
X=(Y+A**B)/(A-B)-(100-Y)/5*B
print(X)

#PROBLEMA 19
print("Ingrese el valor del 1er lado :")
L1=int(input())
print("Ingrese el valor del 2er lado :")
L2=int(input())
print("Ingrese el valor del 3er lado :")
L3=int(input())
print("Ingrese el valor del 4er lado :")
L4=int(input())
print("Ingrese el valor del 5er lado :")
L5=int(input())
print("Ingrese el valor del 6er lado :")
L6=int(input())
print("Ingrese el valor del 7er lado :")
L7=int(input())
print("Ingrese el valor del 8er lado :")
L8=int(input())
P=L1+L2+L3+L4+L5+L6+L7+L8
print("El perimetro es:", P)

#PROBLEMA 20
#SOLUCIÓN SACADA DE GOOGLE
numero = int(input("Ingrese en numero:"))
tmpnumero=numero
dig=int(0)
suma=0;
while(tmpnumero!=0):
    dig=int(tmpnumero % 10)
    suma+=dig
    tmpnumero=int(tmpnumero/10)
print("La suma de los digitos de ",numero," es ",suma)

#PROBLEMA 21




#PROBLEMA 22
print("Ingrese las 1ra nota")
N1=int(input())
print("Ingrese las 2ra nota")
N2=int(input())
print("Ingrese las 3ra nota")
N3=int(input())
print("Ingrese las 4ra nota")
N4=int(input())
P=(N1+N2+N3+N4)/4
print("El promedio es:",P)

#PROBLEMA 23
print("Ingrese el valor del Volumen")
V=int(input())
print("Ingrese el numero de moles")
n=int(input())
print("Ingrese la temperatura")
T=int(input())
R=0.082
P=(n*R*T)/V
print("La presion es:",P)

#PROBLEMA 24




#PROBLEMA 25
print("Ingrese el numero en pulgadas a convertir")
P=int(input())
YD=P*(1/36)
print("Su equivalente en yardas es:",YD)


#PROBLEMA 26
print("Ingrese el valor en galones a convertir")
gal=float(input())
pc=gal*(0.133681/1)
print("Su equivalente en pies cubicos es:",pc)

#PROBLEMA 27



#PROBLEMA 28
print("Ingrese su sueldo neto:")
S=int(input())
M=S*0.3
V=S*0.05
C=S*0.1
print("Por mantenimiento usted debe entregar:",M)
print("Por vestimenta usted debe entregar:",V)
print("Por educación usted debe entregar:",C)

#PROBLEMA 29


#PROBLEMA 30
print("Si hay 3000 litros de capacidad")
H=18000/0.225
print("El tanque tardara en llenarse en horas:",H)

#PROBLEMA 31
print("Ingrese los grados Celcius")
C=int(input())
print("Ingrese el valor de F")
F=int(input())
K=C+273.15
R=F+459.67
print("El equivalente en grados Kelvin y Ranking respectivamente es:",K, R)

