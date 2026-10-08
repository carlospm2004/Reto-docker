alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]


def calcular_media(alumnos):
    """Calcula y devuelve la nota media de una lista de alumnos.

    Si la lista está vacía, devuelve 0.
    """
    if not alumnos:
        return 0

    total_notas = sum(alumno["nota"] for alumno in alumnos)
    return total_notas / len(alumnos)


contador_aprobados = 0

for alumno in alumnos:
    if alumno["nota"] >= 5.0:
        print(f"El alumno {alumno['nombre'].upper()} ha aprobado con una nota de {alumno['nota']}")
        contador_aprobados += 1
    else:
        print(f"El alumno {alumno['nombre'].upper()} ha suspendido con una nota de {alumno['nota']}")

print(f"El número de alumnos aprobados es: {contador_aprobados}")
print(f"El número de alumnos suspendidos es: {len(alumnos) - contador_aprobados}")
print(f"El número de alumnos totales es: {len(alumnos)}")

media_grupo = calcular_media(alumnos)
print(f"La media del grupo es: {media_grupo:.2f}")
