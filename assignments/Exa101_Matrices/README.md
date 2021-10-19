![Tec de Monterrey](../../images/logotecmty.png)
# Multiplos de 3

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():  
  pass

if __name__ == '__main__':
    main()
```

<h3>Multiplos de 3</h3>
Desarrolla la función leer_matriz para leer la matriz, la cual recibe el número de renglones (num_ren). <br>
En la función se deberán pedir los renglones, cada renglon que se solicita tiene el siguiente formato: 
2*45*1, es decir cada uno de los números va separado por un "*"<br>
La función debe regresar la matriz con los números en string. <br><br>

Desarrolla la función convierte_matriz_enteros para convertir los numeros (string) a enteros, la función recibe como parámetro de entrada la matriz con los datos y regresa la matriz ya con los números enteros (int)<br><br>

Desarrolla la función multiplos_tres que recibe una matriz de enteros y regresa una lista que contiene los números que son múltiplos de 3 <br><br>

El programa deberá: <br>
1.- Solicitar la cantidad de renglones<br>
2.- Llamar la función leer_matriz  (el usuario ingresa los renglones correspondientes)<br>
3.- Llamar a la función convierte_matriz_enteros <br>
4.- Imprimir la matriz de enteros "print (matriz)" <br>
5.- Llamar a la función multiplos_tres <br>
6.- Imrpimir la lista con los multiplos de tres  "print(multiplos_3)"<br>



Entrada <br>
Número de renglones de la matriz<br>
Los datos de la matriz que son renglones separados por un "*" <br>

Salida<br>
Una matriz con los enteros ingresados<br>
Una lista que contiene los números que son multiplos de 3 <br>

Ejemplo1 de ejecución del programa:<br>
```
3   <--- cantidad de renglones o filas 
6*7*9  <--- cada uno de los renglones
8*12*3
15*21*-1  
```
### Salida
```      
[[6, 7, 9], [8, 12, 3], [15, 21, -1]]   <--- Matriz con los números enteros
[6, 9, 12, 3, 15, 21]  <--- Lista con los números que son múltiplos de 3 
```

Ejemplo2 de ejecución del programa:<br>
```
2
8*7*6*5
4*5*20*7
```
### Salida
```
[[8, 7, 6, 5], [4, 5, 20, 7]]
[6]   
```

NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.
NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

