import sys

from procesar_stats import mindato, maxdato, promedio, procesar_archivo

# Datos de prueba
data = [0.25, 0.0, 0.05, 3.34, 0.62, 0.1, 0.36, 0.05, 0.05, 0.05]

# Pruebas usando assert
assert mindato(data) == 0.0, "Error en mindato"
assert maxdato(data) == 3.34, "Error en maxdato"
assert abs(promedio(data) - 0.487) < 0.001, "Error en promedio"  # Ajuste para precisión

# Prueba para procesar_archivo
def test_procesar_archivo():
    # Simular un archivo de stats
    with open('test_stats.txt', 'w') as f:
        f.write("User: [0.25, 0.0, 0.05, 3.34, 0.62, 0.1, 0.36, 0.05, 0.05, 0.05]\n")
        f.write("Nice: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]\n")
        f.write("System: [0.56, 0.4, 0.46, 4.91, 1.65, 0.46, 0.71, 0.66, 0.35, 0.35]\n")
        f.write("IOWait: [0.0, 0.05, 0.0, 0.0, 0.05, 0.0, 0.05, 0.0, 0.0, 0.05]\n")
        f.write("Steal: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]\n")
        f.write("Idle: [99.19, 99.55, 99.49, 91.75, 97.68, 99.44, 98.88, 99.29, 99.6, 99.55]\n")
    procesar_archivo('test_stats.txt')

test_procesar_archivo()

print("Todas las pruebas pasaron exitosamente!")
