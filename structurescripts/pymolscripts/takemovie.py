from pymol import cmd, stored, math
from pathlib import Path
	
def takemovie():
    Path("mov").mkdir(parents=True,exist_ok=True)
    cmd.mset("1 x 360")
    cmd.bg_colour(color="white") 
    cmd.set("ray_opaque_background", 1)
    cmd.util.mroll(1,360,1)
    cmd.viewport(1024, 768)
    cmd.set("ray_trace_frames", 1) 
    cmd.mpng("mov/out")
cmd.extend("takemovie", takemovie)
