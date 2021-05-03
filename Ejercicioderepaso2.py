nombre = str (input ('Ingrese nombre del alumno '))
n1 = int (input('Ingrese nota del parcial 1 '))
n2 = int (input('Ingrese nota del parcial 2 '))
n3 = int (input('Ingrese nota del parcial 3 '))

prom = (n1+n2+n3)/3
if (n3 >= 6) and (prom >= 6):
    print ('Aprobado')
else: 
    print ('Desaprobado')

print ('El alumno', nombre , 'desaprobo la materia con' , prom)

