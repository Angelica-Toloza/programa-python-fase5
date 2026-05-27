# ==========================================
# FASE 5 - FUNDAMENTOS DE PROGRAMACIÓN
# Problema 5
# ==========================================

# Función para calcular total y clasificación
def calcular_jornada(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario estándar"

    return total, clasificacion


# Matriz de datos
recursos = [
    ["Ana", 8, 8, 9, 9, 8],
    ["Luis", 7, 7, 7, 7, 7],
    ["Carlos", 9, 9, 8, 8, 9],
    ["Marta", 6, 7, 6, 7, 6]
]

print("===================================")
print("REPORTE DE HORAS SEMANALES")
print("===================================")

# Recorrer matriz
for recurso in recursos:

    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_jornada(horas)

    print(f"Nombre: {nombre}")
    print(f"Total horas: {total}")
    print(f"Clasificación: {clasificacion}")
    print("-----------------------------------")