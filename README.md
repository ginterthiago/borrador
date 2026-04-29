[mediana = [],.py](https://github.com/user-attachments/files/27220424/mediana.py)
mediana = [],
sumatoria = 0
contador = 0

no_se_corta = True
while no_se_corta: 
    numero = int(input("Ingrese un numero(00 para finalizar)"))
    if numero == 00:
        no_se_corta = False
    else: 
        sumatoria += numero
        contador+=1 
        mediana.append(numero)


if contador == 0:
    print("No se ingresaron numeros")
else:
    print(f"el promedio es igual a: "{sumatoria/contador})
    print(f"La suma total es igual a: " {sumatoria})

    print(f"")

mediana.sort()
if contador % 2 == 1:
    valor_mediana = mediana[contador// 2]
else:
    medio1 = mediana[(contador // 2)-1]
    medio2 = mediana[contador// 2]
    valor_mediana = (medio1 + medio2)/2

print  (f"La mediana es igual a: "{valor mediana})
