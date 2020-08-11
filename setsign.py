from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,0,"偷鞋亂丟很無理","無教也該有個底","既然你娘不管你","逮到他媽修理你")