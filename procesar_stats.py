import sys


def mindato(data):
    return min(data)

def maxdato(data):
    return max(data)

def promedio(data):
    return sum(data) / len(data)

def procesar_archivo(stats):
    with open(stats, 'r') as file:
        data = {"User": [], "Nice": [], "System": [], "IOWait": [], "Steal": [], "Idle": []}
        capturing_data = False
        for line in file:
            if 'User:' in line:
                capturing_data = True
            if capturing_data:
                for key in data.keys():
                    if line.startswith(key):
                        parts = line.strip().split(':')[1].strip().strip('[]').split(',')
                        data[key] = [float(part) for part in parts]

        if not all(data.values()):  # Verificar si todas las listas tienen datos válidos
            print("Error: El archivo no contiene datos válidos.")
            return

        for key in data:
            min_valor = mindato(data[key])
            max_valor = maxdato(data[key])
            promedio_valor = promedio(data[key])
            print(f"{key} - Minimo: {min_valor}, Maximo: {max_valor}, Promedio: {promedio_valor}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python procesar_stats.py stats")
    else:
        archivo = sys.argv[1]
        procesar_archivo(archivo)
