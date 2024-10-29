import sys

# Funciones para obtener el mínimo, máximo y promedio
def mindato(data):
    return min(data)

def maxdato(data):
    return max(data)

def promedio(data):
    return sum(data) / len(data)

# Función para procesar el archivo stats
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

    return data

# Función para buscar información según la métrica y el tipo de valor
def buscar_informacion(metrica, tipo):
    data = procesar_archivo('stats')
    
    if metrica not in data:
        print(f"Métrica {metrica} no encontrada.")
        return
    
    if tipo == 'minimo':
        valor = mindato(data[metrica])
    elif tipo == 'maximo':
        valor = maxdato(data[metrica])
    elif tipo == 'promedio':
        valor = promedio(data[metrica])
    else:
        print(f"Tipo {tipo} no reconocido.")
        return
    
    print(f"{metrica.capitalize()} - {tipo.capitalize()}: {valor}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python buscar_informacion.py <metrica> <tipo>")
    else:
        metrica = sys.argv[1].capitalize()
        tipo = sys.argv[2].lower()
        buscar_informacion(metrica, tipo)
