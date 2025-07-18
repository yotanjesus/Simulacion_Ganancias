import numpy as np
import matplotlib.pyplot as plt

# Simulación de datos de ganancias
def generar_datos():
    ganancias_anuales = np.random.randint(50000, 100000, size=5)  # Últimos 5 años
    ganancias_mensuales = np.random.randint(4000, 10000, size=12)  # Últimos 12 meses
    ganancias_diarias = np.random.randint(100, 500, size=30)  # Últimos 30 días
    ganancias_horarias = np.random.randint(10, 50, size=24)  # Últimas 24 horas
    return ganancias_anuales, ganancias_mensuales, ganancias_diarias, ganancias_horarias

# Función para graficar
def graficar_datos(ganancias, titulo, etiquetas_x, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(etiquetas_x, ganancias, color='lightblue', edgecolor='black')
    plt.title(titulo, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Generar datos simulados
ganancias_anuales, ganancias_mensuales, ganancias_diarias, ganancias_horarias = generar_datos()

# Graficar ganancias anuales
años = [f"Año {i}" for i in range(1, 6)]
graficar_datos(ganancias_anuales, "Ganancias Anuales", años, "Años", "Ganancias (USD)")

# Graficar ganancias mensuales
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
graficar_datos(ganancias_mensuales, "Ganancias Mensuales", meses, "Meses", "Ganancias (USD)")

# Graficar ganancias diarias
días = [f"Día {i}" for i in range(1, 31)]
graficar_datos(ganancias_diarias, "Ganancias Diarias", días, "Días", "Ganancias (USD)")

# Graficar ganancias horarias
horas = [f"{i}:00" for i in range(24)]
graficar_datos(ganancias_horarias, "Ganancias Horarias", horas, "Horas", "Ganancias (USD)")
