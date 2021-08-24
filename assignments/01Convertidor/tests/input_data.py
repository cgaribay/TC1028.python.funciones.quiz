# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["1", "1"],
            ["1. pies a cm, 2. pulgadas a cm, 3. yardas a cm", "Introduce una opcion: ", "Introduce la cantidad: ", "30.48"],
            "No funciona la conversión pies a centímetro",
        ),
        # Test case 2
        (
            ["2", "1"],
            ["1. pies a cm, 2. pulgadas a cm, 3. yardas a cm", "Introduce una opcion: ", "Introduce la cantidad: ", "2.54"],
            "No funciona la conversión pulgadas a centímetro",
        ),
        # Test case 3
        (
            ["-5", "1"],
            ["1. pies a cm, 2. pulgadas a cm, 3. yardas a cm", "Introduce una opcion: ", "Introduce la cantidad: ", "Error"],
            "No imprimes 'Error' cuando eligen una opción inválida",
        ),
        # Test case 4
        (
            ["3", "1"],
            ["1. pies a cm, 2. pulgadas a cm, 3. yardas a cm", "Introduce una opcion: ", "Introduce la cantidad: ", "91.44"],
            "No funciona la conversión yardas a centímetro",
        ),
    ]
