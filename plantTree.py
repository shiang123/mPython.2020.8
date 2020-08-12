from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()

def plantTree(time):
    for j in range(time):
        mc.setBlocks(x+10,y+5,z+1,x-10,y+3,z-1,18)
       
   
        mc.setBlocks(x,y,z,x,y+4,z,17)
        mc.setBlocks(x+2,y,z,x+2,y+4,z,17)

        
        
plantTree(8)
