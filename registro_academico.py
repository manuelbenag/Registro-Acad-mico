#Registrar datos de 15 alumnos.

##Datos requeridos:
#Nombre del alumno (convertir a mayúsculas).
#Edad (entre 17 y 25).
#Nota final (de 0 a 10).
#Año de cursada (1, 2, 3 o 4).

#Resultados:
#Promedio de notas de los estudiantes de 2º año.
#Nombre del alumno con la nota más alta.
#Cantidad de alumnos aprobados (nota ≥ 6).
#Porcentaje de estudiantes de 4º año con nota inferior a 4.
#Mostrar mensaje: "Candidato a beca" si obtuvo nota 10 y tiene menos de 20 años.

#VARIABLES
#PROMEDIO NOTAS - ESTUDIANTES 2° AÑO
acumulador_notas = 0
contador_notas = 0
promedio_notas_2 = None

#NOMBRE ALUMNO - NOTA MÁS ALTA
nota_alta = None

#CANTIDAD ALUMNOS APROBADOS - (NOTA >= 6)
contador_notas = 0

#PORCENTAJE DE ESTUDIANTES DE 4°AÑO CON NOTA INFERIOR A 4
total_cuarto = 0
cuarto_nota_menos_de_4 = 0

alumnos = 15

for i in range (alumnos):

    #NOMBRE - ALUMNO
    nombre_alumno = input("Ingrese el nombre del alumno; ").upper()
    print (f"Nombre en mayusculas; {nombre_alumno}")

    #EDAD - ALUMNO
    edad = int(input("Ingrese la edad del alumno. (Entre 17 y 25 años); "))
    while edad < 17 or edad > 25:
        print ("Edada inválida.")
        edad = int(input("Ingrese nuevamente la edad. (Entre 17 y 25 años); "))

    #NOTA - ALUMNO
    nota = float(input("Ingrese la nota del alumno. (De 0 a 10); "))
    while nota < 0 or nota > 10:
        print ("Nota inválida.")
        nota = int(input("Ingrese nuevamente una nota. (De 0 a 10); "))
    
    #AÑO - CURSADA
    año = int(input("Ingrese el año de cursada. (1, 2, 3, o 4); "))
    while año < 1 or año > 4:
        print ("Año inválido.")
        año = int(input("Ingrese el año de cursada nuevamente. (1, 2, 3, o 4); "))

    #PROMEDIO NOTAS - ESTUDIANTES 2° AÑO
    if año == 2:
        acumulador_notas = acumulador_notas + nota
        contador_notas += 1

    if contador_notas > 0:
        promedio_notas_2 = acumulador_notas / contador_notas
    else:
        promedio_notas_2 = None

    #NOMBRE ALUMNO - NOTA MÁS ALTA
    if nota_alta is None or nota > nota_alta:
        nota_alta = nota
        
        nombre_alumno_nota_alta = nombre_alumno
    
    #CANTIDAD ALUMNOS APROBADOS - (NOTA >= 6)
    if nota >= 6:
        contador_notas += 1
    
    #PORCENTAJE DE ESTUDIANTES DE 4°AÑO CON NOTA INFERIOR A 4
    if año == 4:
        total_cuarto += 1
        if nota < 4:
            cuarto_nota_menos_de_4 += 1
    
    if total_cuarto > 0:
        porcentaje = (cuarto_nota_menos_de_4 / total_cuarto) * 100
    else:
        porcentaje = 0        
    



print ("--------------------------------------------------- RESULTADOS ---------------------------------------------------")

if promedio_notas_2 is not None:
    print (f"El promedio de las notas de los estudiantes de 2°año es de; {promedio_notas_2: .2f}.")
else:
    print ("No hubo notas de los alumnos de 2°año.")

print (f"El nombre del alumno con la nota más alta es; {nombre_alumno_nota_alta} con una nota de; {nota_alta}.")

print (f"Cantidad de notas aprobadas mayores o iguales a 6; {contador_notas}.")

print (f"El porcentaje de estudiantes de 4º año con nota inferior a 4 es; {porcentaje: .2f}%")

if nota == 10 and edad < 20:
    print ("Candidato a beca.")










