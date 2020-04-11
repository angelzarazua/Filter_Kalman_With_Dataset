# Filtro Kalman para reducción del filtro

Este proyecto tiene el fin de filtrar una serie de datos que un sensor ha recopilado.
En principio he trabajado con los datos de *Humedad relativa*, pero funcionaría con cualquier tipo de datos
(el ejemplo de la plantilla se encuentra en shared en formato .csv).

## Getting Started

Simplemente elije el dataset con el que quieres hacer las pruebas cambiando Δ y Q, que son los errores.
Toda la información se encuentra en el pdf.

### Installing

```
Python > 3.3.7
```

Ejecutar el programa tal que:

```
python *main.py* (nombre del archivo)
```

O ejecutar programa desde visual studio.

## Built With

* [Numpy](https://numpy.org/) - NumPy is the fundamental package for scientific computing with Python. It contains among other things
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - The Tkinter module (“Tk interface”) is the standard Python interface to the Tk GUI toolkit.
* [CSV](https://docs.python.org/3/library/csv.html) - The csv module implements classes to read and write tabular data in CSV format.
* [Matplotlib](https://matplotlib.org/index.html) - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

## Authors

Gracias a: **zziz**  -[Kalman Filter implementation in Python using Numpy only in 30 lines.](https://github.com/zziz/kalman-filter)-

#### Output
![Result](https://i.ibb.co/NWnWcyH/1.png)
![Result](https://i.ibb.co/Lty7tzn/1-1.png)
![Result](https://i.ibb.co/F4wzKxX/2.png)
![Result](https://i.ibb.co/7rhsWLy/2-1.png)
