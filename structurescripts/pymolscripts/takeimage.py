from pymol import cmd, stored, math
import time
	
def takeimage():
    cmd.ray(2400,2400)
    cmd.set('ray_shadows','off')
    cmd.png("/tmp/{}.png".format(time.ctime(), dpi=300))

cmd.extend("takeimage", takeimage);
