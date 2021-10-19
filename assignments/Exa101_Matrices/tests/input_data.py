# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["3", "3*-2*4*7", "2*3*4*6", "9*12*15*2"],
        ["", "", "", "", "[[3, -2, 4, 7], [2, 3, 4, 6], [9, 12, 15, 2]]",
            "[3, 3, 6, 9, 12, 15]"],
        "Verifica los requerimientos que se solicitan"
    ),
    # Test case 2
    (
        ["4", "7*8*9*10*11", "1*2*3*4*5", "7*6*5*4*3", "6*7*5*3*18"],
        ["", "", "", "", "", "[[7, 8, 9, 10, 11], [1, 2, 3, 4, 5], [7, 6, 5, 4, 3], [6, 7, 5, 3, 18]]",
            "[9, 3, 6, 3, 6, 3, 18]"],
        "Verifica los requerimientos que se solicitan"
    ),
    # Test case 3
    (
        ["1", "1*2*3*4*5*6"],
        ["", "", "[[1, 2, 3, 4, 5, 6]]",
            "[3, 6]"],
        "Verifica los requerimientos que se solicitan"
    ),

]
