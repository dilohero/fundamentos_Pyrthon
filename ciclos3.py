promedio, total, contar =0.0, 0, 0

print ('Introduzca la nota de un estudiante. presiones -1 para salir')
grado = int ( input ())
while grado != -1:
     total = total + grado
     contar = contar + 1
     print (' Introduzca la nota del estudiante, -1 para salir')
     grado = int ( input ())
     
else:
     promedio = total / contar
     print (' Promedio del grado escolar es : ', str (promedio))
     
     