# Ejercicio 005: Teletransportarse al un punto especifico con floats
# Este ejercicio funciona mejor si primer el usuario se coloca en un punto especifico
# Como sobre una fence de madera, y toma esas coordenadas. 

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Declarar x y y z pero como floats
# Como el mundo es flat la Y no tiene que ser tal alta
x = 25.5
y = 10.7
z = 25.5

# Cambiar la posición del jugador
mc.player.setTilePos(x, y, z)
