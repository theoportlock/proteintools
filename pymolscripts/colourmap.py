from pymol import cmd, stored, math
	
def colourmap ():
    cmd.show_as("cartoon")
    cmd.spectrum("b","blue_red", "n. CA ",minimum=0,maximum=1)
    cmd.recolor()

cmd.extend("colourmap", colourmap);
