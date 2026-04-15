TEXTO_NOMBRE_ALUMNO = "Ingrese el nombre del Alumno (): "
TEXTO_EDAD_ALUMNO = "Ingrese la edad del Alumno (): "
MENSAJE_ERROR_EDAD = "Error rn la Edad (): "

alumno1_nombre = input(TEXTO_NOMBRE_ALUMNO.format(1))
try:
   alumno_edad = int(input(TEXTO_EDAD_ALUMNO.format(1)))
except ValueError:
    print(MENSAJE_ERROR_EDAD.format(1))
    alumno1_edad = "Error en Ingreso"  

alumno2_nombre = input(TEXTO_NOMBRE_ALUMNO.format(2))
try:
   alumno2_edad = int(input(TEXTO_EDAD_ALUMNO.format(2)))
except ValueError:
    print(MENSAJE_ERROR_EDAD.format(2))
    alumno2_edad = "Error en Ingreso"

alumno3_nombre = input(TEXTO_NOMBRE_ALUMNO.format(3))
try: 
   alumno3_edad = int(input(TEXTO_EDAD_ALUMNO.format(3)))
except ValueError: 
    print(MENSAJE_ERROR_EDAD.format(3))
alumno3_edad = "Error en Ingreso"
