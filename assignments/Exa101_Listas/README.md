![Tec de Monterrey](../../images/logotecmty.png)
# Listas, multiplicación x 2
### Tema Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  pass

if __name__ == '__main__':
    main()
```

Escribe un programa que primero lea la cantidad del límite inferior y después lea el límite superior. <br>
Si el límite inferior es menor que 1 o si el limite superior no es mayor que el limite inferior, se deberá mostrar el mensaje: "Error en los datos"<br>

Posteriormente, el programa debe crear una lista, empezando con el límite inferior y terminando con el límite superior. <br>
El sistema deberá imprimir la lista y la lista con todos los elementos multiplicados por 2. 

## Entrada
Un número entero que representa el límite inferior y un número que representa el límite superior

## Salida
Dos listas. <br>
Una lista con los valores de la lista empezando con el límite inferior y terminando con el límite superior<br>
La segunda lista debe contener todos los elementos multiplicados por 2.
## Ejemplo1 de ejecución del programa:
### Entrada
```
1
5
```
### Salida
```
Error en los datos
```

## Ejemplo2 de ejecución del programa:
### Entrada
```
3
7
```
### Salida
```
[3, 4, 5, 6, 7]
[6, 8, 10, 12, 14]
```

## Ejemplo3 de ejecución del programa:
### Entrada
```
4
2
```
### Salida
```
Error en los datos
```

No uses letreros para pedir los datos. 

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.
