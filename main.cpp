#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

void mostrarEstadisticas() {
    // Llama al script de Python para procesar el archivo stats
    system("python procesar_stats.py stats");
}

void buscarInformacion(string metrica, string tipo) {
    // Construye el comando para buscar información
    string comando = "python buscar_informacion.py " + metrica + " " + tipo;
    system(comando.c_str());
}

void hacerTest() {
    // Ejecuta el script de prueba de funciones
    int result = system("python test_functions.py");
    if(result == 0)
        cout << "Todas las pruebas pasaron exitosamente!" << endl;
    else
        cout << "Algunas pruebas fallaron." << endl;
}

int main() {
    int opc = 1;
    int ce1, ce2;
    string est1, est2;
    string metrica, tipo;
    cout << "  ________   _______   _________   ___    __   __    ________    _______   _________  " << endl;
    cout << " |        | |       | |         | |   |  |  | |  |  |   __   |  |       | |         | " << endl;
    cout << " |____    | |    ___| |___    __| |   |  |  |_/  |  |  |  |  |  |  |°   | |___    __| " << endl;
    cout << "  ____|   | |   |___      |  |    |   |  |      /   |  |__|  |  |    ___|     |  |    " << endl;
    cout << " |    ____| |    ___|     |  |    |   |  |  | |  |  |   __   |  |  |    |     |  |    " << endl;
    cout << " |   |____  |   |___      |  |    |   |  |  | |  |  |  |  |  |  |  | |  |     |  |    " << endl;
    cout << " |________| |_______|     |__|    |___|  |__| |__|  |__|  |__|  |__| |__|     |__|    " << endl;


    while(opc != 0) {
        cout << "...:: GESTION DE METRICAS DE DISTRIBUICION DE USO DE CPU:::....." << endl;
        cout << "1 - Creacion estadisticas de uso de CPU" << endl;
        cout << "2 - Revision de Estadistica" << endl;
        cout << "3 - Mostrar Estadisticas" << endl;
        cout << "4 - Buscar Informacion por Valor" << endl;
	cout << "5 - Hacer Test" << endl;
        cout << "0 - Salir" << endl;
        cout << "Ingrese Opcion: ";
        cin >> opc;
        
        switch (opc) {
            case 1:
                ce1 = system("./main.sh");
                est1 = ce1 == 0 ? "E Correcta" : "E Incorrecta";
                cout << est1 << endl;
                break;
            case 2:
                ce2 = system("cat stats");
                est2 = ce2 == 0 ? "E Correcta" : "E Incorrecta";
                cout << est2 << endl;
                break;
            case 3:
                mostrarEstadisticas();
                break;
            case 4:                
                cout << "Ingrese la métrica (User, Nice, System, IOWait, Steal, Idle): ";
                cin >> metrica;
                cout << "Ingrese el tipo de búsqueda (minimo, maximo, promedio): ";
                cin >> tipo;
                buscarInformacion(metrica, tipo);
                break;
	           case 5:
		            hacerTest();
		            break;
            case 0:
                cout << "Adios..." << endl;
                break;
            default:
                cout << "Ingrese Opcion Valida" << endl;
                break;
        }
    }
    
    return 0;
}



