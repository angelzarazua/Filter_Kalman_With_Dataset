from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from Kalman import Kalman
import numpy as np
import random
import csv
import copy
import os


# Array que guarda los datos del dataset (Datos reales según Kalman)
datos_x = []
x_filtrada = []  # Array que guarda los datos filtrados según los datos reales
ganancia = []  # Array que guarda la ganacia de Kalman

dt = 0.05  # Delta T
_Q = .000001  # La covarianza del ruido del proceso
F = np.array([
    [1, dt, 0],
    [0, 1, dt],
    [0, 0, 1]])
H = np.array([1, 0, 0]).reshape(1, 3)
Q = np.array([
    [_Q, _Q, 0.0],
    [_Q, _Q, 0.0],
    [0.0, 0.0, 0.0]])
R = np.array([0.5]).reshape(1, 1)

tipo_sensor = ''
directorio = "Datos"
directorioAssets = "Assets"

NO_DATOS = 4000  # Es el número de datos que se quieren procesar


def verificarCarpetas():
    global directorio
    global directorioAssets

    #Si no existen los directorios, los crea
    try:
        os.stat(directorio)
    except:
        os.mkdir(directorio)

    try:
        os.stat(directorioAssets)
    except:
        os.mkdir(directorioAssets)


def llenarDatos():
    try:
        global tipo_sensor

        # Descomentar la línea de abajo si se quiere abrir un cuadro para elegir el archicho deseado
        #rutaArchivo = askopenfilename(initialdir = ".", title = "Cargar CSV", filetypes =(("Document file", "*.csv"), ("all files","*.*")))
        # Si la línea anterior se descomenta, comentar la siguiente
        rutaArchivo = 'shared/HumRel.csv'
        print('Ruta del archivo', rutaArchivo)

        with open(rutaArchivo) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            # print(csv_file.readline())
            for row in csv_reader:
                if line_count == 0:  # Solo entrar la primera vez, indica las columnas del dataset.
                    print(f'Column names are: {", ".join(row)}')
                    tipo_sensor = row[1]
                    line_count += 1
                elif line_count != NO_DATOS + 1: # +1 Porque la primera vez lee las columnas.
                    # Si el dato leído es vacío, lo convierte en cero para que el programa con se rompa.
                    if not row[1]:
                        row[1] = '0'
                    # Los datos se convierten en números, ya que desde el archivo .csv los lee como strings
                    # A su vez, va llenando los datos en el array
                    datos_x.append(float(row[1]))
                    line_count += 1
                else:
                    break
            csv_file.close()
    except IOError:
        print('An error occurred trying to read the file.')
    except ValueError:
        print('Non-numeric data found in the file.')
    except ImportError:
        print("NO module found")
    except KeyboardInterrupt:
        print('You cancelled the operation.')
    except EOFError:
        print('Why did you do an EOF on me?')


def graficar():  # Función que grafica los datos obtenidos
    global directorioAssets

    # Esta gráfica grafica los datos del dataset y los datos filtrados.
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(range(len(datos_x)), datos_x, label='Datos')
    ax.plot(range(len(x_filtrada)), np.array(x_filtrada), label='Filtrado')
    ax.set_ylabel(tipo_sensor)
    ax.set_xlabel('Datos')
    ax.set_title('dt = ' + str(dt) + '   Q = ' + str(_Q))
    ax.legend()

    fig2, ax2 = plt.subplots()  # Esta grafica la gancia de Kalman
    ax2.grid()
    ax2.plot(range(len(ganancia)), ganancia, label='Ganancia')
    ax2.set_title('Ganancia Kalman, ' + tipo_sensor)
    ax2.legend()

    # Guarda la primer gráfica con el nombre de los errores que se haya puesto; en el directorio 'Assets'
    fig.savefig(directorioAssets + "/" + tipo_sensor +
                " dt_" + str(dt) + " Q_" + str(_Q) + ".png")
    # Guarda la segunda gráfica con el nombre de los errores que se haya puesto; en el directorio 'Assets'
    fig2.savefig(directorioAssets + "/Ganancia_Kalman " +
                 tipo_sensor + " dt_" + str(dt) + " Q_" + str(_Q) + ".png")

    plt.show()
    plt.show()


if __name__ == "__main__":
    # Crea el objeto Kalman pasando 4 datos como parámetros.
    ka = Kalman(F, Q, H, R)
    i = 1  # Contador para guardar en el txt e identficar las iteraciones

    llenarDatos()
    verificarCarpetas()
    archivo = open(directorio + "/Datos_" + tipo_sensor + " dt_" +
                   str(dt) + " Q_" + str(_Q) + ".txt", "w", encoding='utf-8')
    archivo.write("I, Z,   Z_f,   dt = " + str(dt) +
                  "\t Q = " + str(_Q) + "\n")

    for dato_z in datos_x:
        x_f = np.dot(H,  ka.predecir())[0]
        x_filtrada.append(x_f)
        ganancia.append(ka.actualizar(dato_z)[0])
        archivo.write(f'{i}, {dato_z}, {x_f}\n')
        i += 1

    archivo.close()
    graficar()
