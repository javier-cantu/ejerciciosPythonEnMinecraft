# Ejercicio 016_setBlocksCubosClear
# Crear un cubo grande de aire con 2 coordenadas para limpiar la zona de bloques. 

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Necesitamos importar time
import time

##########################################
# Primero  determinamos la coordenada incial
x = -20
y = 4
z = -20

#Creamos la coordenada final
x2 = 20
y2 = 20
z2 = 20

# Tipo de Bloque 0 es el ID de aire
blockType = 0

# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)
