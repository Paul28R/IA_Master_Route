import sys
# esta linea se ejecuta siempre
print("--- Iniciando analisis de errores ---")


for line in sys.stdin:
# Transformamos el texto a mayusculas para notar el cambio
    print(f"Found: {line.strip().upper}")
# Process each error line
print("Finished analyzing errors.")
