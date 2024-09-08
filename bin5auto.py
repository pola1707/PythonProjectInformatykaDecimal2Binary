decimal_number = 42
binary_number = ""
if decimal_number == 0:
    binary_number = "0"
else:
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2

print(f"Liczba binarna: {binary_number}")
