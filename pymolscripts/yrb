#A script to highlight hydrophobicity and charge on protein surfaces
#DHS065 Hagemans et al YRB script
#created by Dominique Hagemans and Ianthe A.E.M. van Belzen, July 2015
#Rudiger group CPC, Utrecht University

#yellow: C, CH, CH2, CH3 groups that are not bound to N or O groups.
#red: negatively charged atoms
#blue: positively charged atoms
#grey: backbone, polar groups and remaining atoms

#usage:
#(1) save this script as file with a .py extension at desirable location
#(2) open your structure in pymol and change to surface view.
#(3) run this script: File --> Run --> DHS065 Hagemans et al YRB script
#(4) give the command to colour all structures or a specific structure:
#(4 a) "yrb" to colour all structures
#(4 b) "yrb 'designation'" to colour only that specific structure

from pymol import cmd
 
def yrb(selection='all'):

	cmd.remove("hydro")
	cmd.set_color('yellow',[0.950,0.78,0.0])
	cmd.set_color('grey',[0.95,0.95,0.95])
	cmd.set_color('red',[1.0,0.4,0.4])	
	cmd.set_color('blue',[0.2,0.5,0.8])	
	
	mapping = {}
	mapping['arg'] = [ ('NE,NH2,NH1', 'blue'), ('CD,CZ', 'grey'), ('CG', 'yellow') ]
	mapping['asn'] = [ ('CG,OD1,ND2', 'grey') ]
	mapping['asp'] = [ ('CG', 'grey'), ('OD2,OD1', 'red')  ]
	mapping['cys'] = [ ('SG', 'grey') ]	
	mapping['gln'] = [ ('CG', 'yellow'), ('CD,OE1,NE2', 'grey') ]
	mapping['glu'] = [ ('CG', 'yellow'), ('CD', 'grey'), ('OE1,OE2', 'red') ]
	mapping['his'] = [ ('CG,CD2,ND1,NE2,CE1', 'grey') ]	
	mapping['ile'] = [ ('CG1,CG2,CD1', 'yellow') ]
	mapping['leu'] = [ ('CG,CD1,CD2', 'yellow') ]
	mapping['lys'] = [ ('CG,CD', 'yellow'), ('CE', 'grey'), ('NZ', 'blue') ]
	mapping['met'] = [ ('CG,CE', 'yellow'), ('SD', 'grey') ]
	mapping['phe'] = [ ('CG,CD1,CE1,CZ,CE2,CD2', 'yellow') ]
	mapping['pro'] = [ ('CG', 'yellow'), ('CD', 'grey') ]
	mapping['ser'] = [ ('CB,OG', 'grey') ]
	mapping['thr'] = [ ('CB,OG1', 'grey'), ('CG2', 'yellow') ]
	mapping['trp'] = [ ('CG,CD2,CZ2,CH2,CZ3,CE3', 'yellow'), ('CD1,NE1,CE2', 'grey') ]
	mapping['tyr'] = [ ('CG,CE1,CD1,CE2,CD2', 'yellow'), ('CZ,OH', 'grey') ]
	mapping['val'] = [ ('CG1,CG2', 'yellow') ]

	obj_list = cmd.get_names('objects')
	for obj in obj_list:
		if (obj == selection or selection == 'all'):
			cmd.color('grey','(n. N,C,CA,O and ' + obj + ')')
			cmd.color('yellow','(n. CB and ' + obj + ')')
			
			for key in mapping:
				for (atom, color) in mapping[key]:
					cmd.color(color, '( n. ' + atom + ' and r. ' + key + ' and ' + obj + ' )')

cmd.extend('yrb',yrb)
