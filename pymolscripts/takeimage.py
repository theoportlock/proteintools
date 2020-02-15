from pymol import cmd, stored, math
	
def takeimage ():
    cmd.ray(2400,2400)
    cmd.png("output.png",dpi=300)

cmd.extend("takeimage", takeimage);

