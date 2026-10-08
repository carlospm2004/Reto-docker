alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]

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

def calcular_promedio(alumnos):
    """_summary_

    Args:
        alumnos (list): lista de diccionarios con la información de los alumnos

    Returns:
        float: la nota promedio de los alumnos
    """
    if len(alumnos) == 0:
        return 0
    total_notas = sum(alumno["nota"] for alumno in alumnos)
    promedio = total_notas / len(alumnos)
    return promedio

promedio_general = calcular_promedio(alumnos)
print(f"El promedio general de las notas es: {promedio_general:.2f}")