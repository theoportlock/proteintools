from pymol import cmd, stored, math
from pathlib import Path
	
def takemovie ():

    Path("mov").mkdir(parents=True,exist_ok=True)
    cmd.mset("1 x 360")
    cmd.bg_colour(color="white") 
    #cmd.set("ray_trace_mode", 1) 
    #cmd.set("ray_trace_gain", 0.1) 
    #cmd.set("ray_shadow_decay_factor", 0.1) 
    #cmd.set("ray_shadow_decay_range", 2) 
    #cmd.set("antialias", 2)
    #cmd.set("reflect", 0.5)
    #cmd.set("light_count", 10)
    #cmd.set("spec_count", 1)
    #cmd.set("shininess", 100)
    #cmd.set("specular", 1)
    #cmd.set("direct",0)
    #cmd.set("reflect",1.5)
    cmd.set("ray_opaque_background", 1)


    cmd.util.mroll(1,360,1)
    cmd.viewport(1024, 768)
    cmd.set("ray_trace_frames", 1) 

    cmd.mpng("mov/out")

cmd.extend("takemovie", takemovie)
