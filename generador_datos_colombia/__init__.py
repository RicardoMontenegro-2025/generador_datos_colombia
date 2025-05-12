# generador_datos_colombia/generador_datos_colombia/__init__.py

# Importa las funciones principales desde generador.py para que estén disponibles
# directamente al importar 'generador_datos_colombia'
from .generador import crear_base_datos_simulada
from .generador import imprimir  # <--- ¿ESTÁ ESTA LÍNEA PRESENTE?

# Define la versión de tu librería
__version__ = "0.1.1" # O la versión que hayas puesto
