TEXTO_NOMBRE_ALUMNO = "Ingrese el nombre del Alumno (): "
TEXTO_EDAD_ALUMNO = "Ingrese la edad del Alumno (): "
MENSAJE_ERROR_EDAD = "Error rn la Edad (): "

alumno1_nombre = Entrada(TEXTO_NOMBRE_ALUMNO.Formato(1))
Prueba:
    alumno_edad = int(Entrada(TEXTO_EDAD_ALUMNO.Formato(1)))

excepto ValueError: 
      Impreso(MENSAJE_ERROR_EDAD.Formato(1))
      alumno1_edad = "Error en Ingreso"  

alumno2_nombre = Entrada(TEXTO_NOMBRE_ALUMNO.Formato(2))
Prueba:
   alumno2_edad = int(Entrada(TEXTO_EDAD_ALUMNO.Formato(2)))
excepto ValueError: 
    Impreso(MENSAJE_ERROR_EDAD.Formato(2))
    alumno2_edad = "Error en Ingreso"

alumno3_nombre = Entrada(TEXTO_NOMBRE_ALUMNO.Formato(3))
Prueba:
    alumno3_edad = int(Entrada(TEXTO_EDAD_ALUMNO.Formato(3)))
excepto ValueError:
   Impreso(MENSAJE_ERROR_EDAD.Formato(3))
alumno3_edad = "Error en Ingreso"
