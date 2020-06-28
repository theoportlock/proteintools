from pymol import cmd, stored, math
	
def colourmap ():
    cmd.show_as("cartoon")
    cmd.spectrum("b","white_red", "n. CA ",minimum=0,maximum=0.5)
    cmd.recolor()

def colourmapsurface ():
    cmd.show_as("surface")
    cmd.spectrum("b","white_red", "n. CA ",minimum=0,maximum=0.5)
    cmd.set(surface_quality,1)
    cmd.set(solvent_radius,1)
    cmd.recolor()

cmd.extend("colourmap", colourmap)
cmd.extend("colourmapsurface", colourmapsurface)
