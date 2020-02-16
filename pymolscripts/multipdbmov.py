from pymol import cmd, stored, math
from glob import glob
	
def multipdbmov ():

    file_list = glob("cluster*.pdb")

    for file in file_list
       cmd.load(file,"mov")

    cmd.mset("1 -%d -2"%len(file_list))
    cmd.mplay()

cmd.extend("multipdbmov", multipdbmov);

