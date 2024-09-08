decimal_number = int(input()) # Ustalamy liczbę do zamiany

# Reprezentacja binarna za pomocą wbudowanej funkcji `bin`
binary_number = bin(decimal_number)[2:]  # Używamy [2:] do usunięcia prefiksu "0b"

# Wyświetlenie wyniku
print(f"Liczba binarna: {binary_number}")