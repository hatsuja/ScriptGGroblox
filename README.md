# Motor de Generación Procedimental Infinita con Matrices 🚀

Este proyecto aplica conceptos fundamentales de **Álgebra Lineal** (matrices de estado, transformaciones lineales y escalamiento posicional) para construir un generador dinámico de mapas tridimensionales con trampas en **Roblox Studio**, junto con una validación analítica bidimensional en **Google Colab**.

---

## 🛠️ Acceso al Código Fuente

Usa los siguientes botones para navegar directamente a los fragmentos de código del proyecto:

[![Lua Code](https://img.shields.io/badge/Código_en_Roblox-Lua-blue?style=for-the-badge&logo=lua&logoColor=white)](./generacion.lua)
[![Python Code](https://img.shields.io/badge/Código_en_Colab-Python-green?style=for-the-badge&logo=python&logoColor=white)](./generacion.py)

---

## 📊 Relación con el Álgebra Lineal

### 1. Matriz de Estado Dinámica
El mapa no se guarda de forma estática; la memoria del servidor procesa los bloques como una **Matriz Fila Dinámica** de dimensión $1 \times n$:
$$M = \begin{pmatrix} 1 & 1 & 1 & \dots & 1 & 2 & 1 \end{pmatrix}$$
* **Estado 1:** Camino seguro (Bloque Azul)
* **Estado 2:** Bloque Trampa (Bloque Rojo - Elimina al jugador)

### 2. Transformación por Escalar (Homotecia)
Para ubicar físicamente cada elemento en el espacio de coordenadas tridimensional ($X, Y, Z$) sin que se encimen, el sistema multiplica los índices lógicos por una matriz diagonal cargada con el tamaño físico del bloque (`TAMANIO_BLOQUE = 4`):
$$\begin{pmatrix} X \\ Y \\ Z \end{pmatrix} = \begin{pmatrix} 4 & 0 \\ 0 & 4 \end{pmatrix} \cdot \begin{pmatrix} \text{Estado} \\ \text{Índice} \end{pmatrix}$$

---

## 🖥️ Demostración del Sistema

### Renderizado Físico 3D (Roblox Studio)
Cuando el avatar supera el bloque número 20, el algoritmo probabilístico empieza a intercalar celdas con estado de trampa (rojas):

https://github.com/user-attachments/assets/95e23dda-a2b8-443c-86ad-b5f5f2327267

### Validación Analítica (Google Colab / NumPy)
Proyección cartesiana bidimensional que demuestra la correcta distribución de las celdas numéricas leídas desde la memoria por la CPU:

<img width="1272" height="493" alt="Proyección Cartesiana de la Matriz" src="https://github.com/user-attachments/assets/d22bb4 -a5b0-4b0e-94b8-dd372fe66d93" />

---

## 🎓 Autores
* **Desarrollador:** Lex Hatsu (hatsuja)
* **Asignatura:** Álgebra Lineal - Ingeniería en Computación
* **Institución:** Universidad Nacional de Loja (UNL)
* **Docente:** Edwin René Guamán Quinche
