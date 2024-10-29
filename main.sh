#!/bin/bash

# COMANDO 'sar -u 1 20': muestras del uso del CPU cada 10 seg durante 10 segundos.
sar -u 10 10 > cache
python3 -c "
lista = []
with open('cache', 'r') as fichero:
    for linea in fichero:
        if 'CPU' not in linea and 'Linux' not in linea and 'Media' not in linea:  # Filtrar líneas de encabezado y metadata
            parts = linea.split()
            if len(parts) == 8:  # Asegurarse de que la línea tenga 8 elementos
                lista.append({
                    'time': parts[0],
                    'user': float(parts[2].replace(',', '.')),
                    'nice': float(parts[3].replace(',', '.')),
                    'system': float(parts[4].replace(',', '.')),
                    'iowait': float(parts[5].replace(',', '.')),
                    'steal': float(parts[6].replace(',', '.')),
                    'idle': float(parts[7].replace(',', '.'))
                })
times = [m['time'] for m in lista]
user = [m['user'] for m in lista]
nice = [m['nice'] for m in lista]
system = [m['system'] for m in lista]
iowait = [m['iowait'] for m in lista]
steal = [m['steal'] for m in lista]
idle = [m['idle'] for m in lista]
print('........::DISTRIBUICION DEL USO DEL CPU:::::........')
print('TIEMPO DE RECOPILACION DE DATOS')
print('Times:', times)
print('TIEMPO DE CPU UTILIZADO POR PROCESOS DE USUARIOS')
print('User:', user)
print('TIEMPO DE PROCESOS DE -BAJA PRIORIDAD- ')
print('Nice:', nice)
print('TIEMPO DE USO DEL PROCESADOR DEDICADO A TAREAS INTERNAS')
print('System:', system)
print('TIEMPO DEL CPU ESPERANDO QUE SE COMPLETEN OPERACIONES DE ENTRADA/SALIDA')
print('IOWait:', iowait)
print('TIEMPO DE ESPERA DE UNA MAQUINA VIRTUAL, MIENTRAS HYPERVISOR Gestiona otro trabajo')
print('Steal:', steal)

print('TIEMPO INACTIVIDAD DEL CPU')
print('Idle:', idle)
" > stats
rm cache
