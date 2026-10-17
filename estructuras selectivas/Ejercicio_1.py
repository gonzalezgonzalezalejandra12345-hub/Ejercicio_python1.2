'''Determinar si un aprendiz aprueba o desaprueba Algoritmia, sabiendo que aprobará si 
su promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario.''' 

Calificacion1= float (input("Ingrese la primera calificacion:"))
Calificacion2= float (input("Ingrese la segunda calificacion:"))
Calificacion3= float (input("Ingrese la tercera calificacion:"))

Promedio= (Calificacion1 + Calificacion2 + Calificacion3)/3

print("El promedio es:",Promedio)

if Promedio >= 70:
     print("El aprendiz aprobo Algoritmia")
else:
     print("El aprendiz desaprobo Algoritmia")