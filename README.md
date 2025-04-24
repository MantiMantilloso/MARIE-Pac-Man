# MARIE-Pac-Man

Este proyecto es una implementación del clásico juego Pac-Man utilizando el lenguaje ensamblador MARIE (Machine Architecture that is Really Intuitive and Easy). El objetivo principal es demostrar cómo se pueden aplicar conceptos de arquitectura de computadoras y programación de bajo nivel en la creación de un juego interactivo.

## Estructura del Proyecto

El repositorio contiene los siguientes archivos:

- **`code.mas`**: Archivo principal que contiene el código fuente en ensamblador MARIE para el juego Pac-Man.

- **`generadormovimientos.py`**: Script en Python que genera los movimientos del juego, posiblemente utilizado para simular o automatizar ciertas partes del juego.

## Requisitos

Para ejecutar este proyecto, necesitarás:

- El simulador MARIE, que puedes acceder desde [MARIE Simulator](https://marie.js.org/).

- Python 3.x para ejecutar el script `generadormovimientos.py`.

## Opcional
- Se puede generar un nuevo mapa para el juego usando un generador especificamente diseñado para este proyecto, se lo puede acceder desde [Generador Mapas](https://danielalexander27.github.io/pacman-maker-web/)

## Cómo Ejecutar

1. Abre el simulador MARIE.

2. Carga el archivo `code.mas` en el simulador.
3. Si generaste nuevos movimientos o nuevo mapa, cargalos en la sección correspondiente del archivo `code.mas` .

4. Compila y ejecuta el programa dentro del simulador para iniciar el juego.

5. Opcionalmente, puedes ejecutar el script `generadormovimientos.py` para generar movimientos aleatorios.

