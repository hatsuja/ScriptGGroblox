# === SIMULADOR EN GOOGLE COLAB DEL MOTOR INFINITO ===
import numpy as np
import matplotlib.pyplot as plt
import random

# 1. Configuración de escala física (Igual que en Roblox)
TAMANIO_BLOQUE = 4
ultima_posicion_z = 0
contador_bloques = 0

# Creamos listas dinámicas que simularán nuestra matriz en crecimiento
matriz_estados = []      # Guardará 1 (Azul) o 2 (Rojo)
matriz_coordenadas = []  # Guardará la posición Z real de cada bloque

# Función para añadir un nuevo bloque a la estructura matricial
def crear_bloque_en_matriz():
    global ultima_posicion_z, contador_bloques
    contador_bloques += 1
    
    # LÓGICA MATEMÁTICA: Después del bloque 20, hay probabilidad de trampa
    if contador_bloques > 20 and random.randint(1, 4) == 1:
        tipo_bloque = 2 # Estado 2: Trampa Roja
    else:
        tipo_bloque = 1 # Estado 1: Camino Azul
        
    matriz_estados.append(tipo_bloque)
    matriz_coordenadas.append(ultima_posicion_z)
    
    # Desplazamiento lineal por el escalar del tamaño del bloque
    ultima_posicion_z += TAMANIO_BLOQUE

# 2. Inicialización: Generamos los primeros 25 bloques
for _ in range(25):
    crear_bloque_en_matriz()

# Convertimos nuestras listas dinámicas en vectores reales de NumPy
vector_estados = np.array(matriz_estados)
vector_posiciones = np.array(matriz_coordenadas)

# Mostramos la matriz lógica final en la consola de Colab
print("=== MATRIZ DE ESTADOS GENERADA PROCEDIMENTALMENTE ===")
print("Índice de Bloque:", np.arange(1, contador_bloques + 1))
print("Estado del Bloque:", vector_estados)
print("Coordenada Z Real:", vector_posiciones)

# 3. Renderizado gráfico tridimensional simulado (Vista desde arriba)
plt.figure(figsize=(12, 2))
for i in range(len(vector_estados)):
    color = 'dodgerblue' if vector_estados[i] == 1 else 'red'
    # Dibujamos cada celda de la matriz como un cuadrado en el plano cartesiano
    plt.scatter(vector_posiciones[i], 0, color=color, marker='s', s=400, edgecolors='black')

plt.title("Proyección Cartesiana de la Matriz Dinámica (Caminata Infinita)", fontsize=12, fontweight='bold')
plt.xlabel("Eje de Coordenadas Z (Metros en el juego)")
plt.yticks([]) # Ocultamos el eje Y porque caminamos en línea
