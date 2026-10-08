import pytest
from notas import calcular_promedio

def test_calcular_promedio():
    alumnos = [
        {"nombre": "Ana", "nota": 8.5},
        {"nombre": "Luis", "nota": 4.0},
        {"nombre": "Marta", "nota": 7.0},
        {"nombre": "Pablo", "nota": 3.5},
        {"nombre": "Sara", "nota": 9.0},
    ]
    assert calcular_promedio(alumnos) == 6.4