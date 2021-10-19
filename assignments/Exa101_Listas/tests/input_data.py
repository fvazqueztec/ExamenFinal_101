# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
        [3, 7],
        ["", "", "[3, 4, 5, 6, 7]", "[6, 8, 10, 12, 14]"],
        ["La salida no cumple con el caso de prueba\nVerifica los requerimientos"]
    ),
    # Test case 2
    (
        [15, 20],
        ["", "", "[15, 16, 17, 18, 19, 20]", "[30, 32, 34, 36, 38, 40]"],
        ["La salida no cumple con el caso de prueba\nVerifica los requerimientos"]
    ),
    # Test case 3
    (
        [1, 5],
        ["", "", "Error en los datos"],
        ["La salida no cumple con el caso de prueba\nVerifica cuando el numero de elementos es 1 o menor que uno y verifica que el segundo limite sea mayor que el primero"]
    ),
    # Test case 4
    (
        [10, 8],
        ["", "", "Error en los datos"],
        ["La salida no cumple con el caso de prueba\nVerifica cuando el numero de elementos es 1 o menor que uno y verifica que el segundo limite sea mayor que el primero"]
    ),
]
