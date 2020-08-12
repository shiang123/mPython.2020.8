from mcpi.minecraft import Minecraft
import random
import time
mc = Minecraft.create()

pos = mc.player.getPos()

while True:
    x = pos.x+random.uniform(-20,20)
    y = pos.y+random.uniform(-20,20)
    z = pos.z+30
    mc.spawnEntity(x,y,z, 93)
    time.sleep(0.1)