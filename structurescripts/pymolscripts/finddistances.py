"""
DESCRIPTION
Given an object, a reference amino acid and a radius, this scripts calculates pairwise
distances between all atoms in the reference and all atoms that fall within the given range.
Distances are either returned on screen (default) or printed on file.
Distances can be calculated from a single atom only.
Optionally, only atoms that can form H-bonds can be returned (but check distances!)

More information at: PymolWiki
http://pymolwiki.org/index.php/DistancesRH

AUTHOR
Pietro Gatti-Lafranconi, 2012
Please inform me if you use/improve/like/dislike/publish with this script.
CC BY-NC-SA
"""

from pymol import cmd, stored, math
	
def distancesRH (obj, ref, dist, chain=0, output="S", show="N", Hbonds="N", aname="*"):
	"""	
	usage: distancesRH obj, ref, dist, [chain, [output S/P/N, [show Y/N, [Hbonds Y/N, [aname]]]]]
	
	obj: object name, ref:reference aa, dist: radius in A, chain: selected chain
	output: accepts S (screen), P (print) or N (none), default=S
	show: shows distances in pymol window, default=N
	Hbonds: restricts results to atoms that can form Hbonds, default=N
	aname: name of a specific atom in ref (to calculate distances from one atom only)
		
	example: distancesRH 2WHH, 25, 3.2, [B, [S, [N, [Y, [CB]]]]]
	"""
	print ""
	#delete previous selections and displayed distances
	cmd.delete ("dist*")
	cmd.delete ("Atoms")
	cmd.delete ("Residues")
	cmd.delete ("Reference")
	cmd.delete ("Hbonds")
	cmd.delete ("RefAtom")
	#creates and names selections	
	if chain==0: cen=obj
	else: cen=obj+" and chain "+chain
	refA=" and resi "+ref+" and name "+aname
	cmd.select("Reference", "byres "+cen+refA)
	m1=cmd.get_model ("Reference")
	if aname!="*":
		cmd.select("RefAtom", cen+refA)
		m1=cmd.get_model ("RefAtom")
	cmd.select("Atoms", cen+refA+" around "+str(dist)+" and not resi "+ref+" and "+obj)
	cmd.show("nb_spheres", "(Atoms or Reference) and (resn HOH or HET)")
	cmd.select("Residues", "byres Atoms")
	m2=cmd.get_model("Atoms and visible")	
	if Hbonds=="Y":
		cmd.select("__Hbonds1", "Reference and not symbol c")
		if aname!="*":
			cmd.select("__Hbonds1", "RefAtom and not symbol c")
		cmd.select("__Hbonds2", "Atoms and not symbol c")
		cmd.select("Hbonds", "__Hbonds1 or __Hbonds2")
		cmd.show("lines", "Hbonds")
		m1=cmd.get_model ("__Hbonds1")
		m2=cmd.get_model ("__Hbonds2 and visible")	
	
	#controllers	
	if (not (output=="S" or output=="N" or output=="P")) or (not (show=="Y" or show=="N")) or (not (Hbonds=="Y" or Hbonds=="N")):
		print "Malformed input, please try again"
		return
	abort=1
	abort2=0
	mc=cmd.get_model(cen)
	for c0 in range(len(mc.atom)):
		if mc.atom[c0].resi==ref: abort=0
	mc2=cmd.get_model(cen+refA)
	if aname!="*":
		abort2=1
		for c00 in range (len(mc2.atom)):	
			if mc2.atom[c00].name==aname: abort2=0
	if Hbonds=="Y":
		if aname[0]=="C":
			print "Warning: no atoms in the selection can form H-bonds"
			return
	if abort==1: print "Warning: no such residue in the reference object"
	if abort2==1: 
		if abort==0: print "Warning: no such atom in the reference object"
	if abort==1 or abort2==1: return

	#measures distances
	distance2=[]
	distances=[]
	screenOP=""	
	fileOP=""
	for c1 in range(len(m1.atom)):
		for c2 in range(len(m2.atom)):
			if math.sqrt(sum(map(lambda f: (f[0]-f[1])**2, zip(m1.atom[c1].coord,m2.atom[c2].coord))))<float(dist):
				distance=cmd.distance (obj+"//"+m1.atom[c1].chain+"/"+m1.atom[c1].resi+"/"+m1.atom[c1].name, obj+"//"+m2.atom[c2].chain+"/"+m2.atom[c2].resi+"/"+m2.atom[c2].name)
				distances.append(distance)
				screenOP+="%s/%s/%s/%s to %s/%s/%s/%s: %.3f\n" % (m1.atom[c1].chain,m1.atom[c1].resn,m1.atom[c1].resi,m1.atom[c1].name,m2.atom[c2].chain,m2.atom[c2].resn,m2.atom[c2].resi,m2.atom[c2].name, distance)
				fileOP+="%s/%s/%s/%s\t\t\t%s/%s/%s/%s\t\t\t\t%.5f\n"%  (m1.atom[c1].chain,m1.atom[c1].resn,m1.atom[c1].resi,m1.atom[c1].name,m2.atom[c2].chain,m2.atom[c2].resn,m2.atom[c2].resi,m2.atom[c2].name, distance)	
	#last controller
	if len(distances)==0:
		if abort2==0:
			print "Warning: no atoms within the selected range"
		return

	#data outputs
	if output=="N": print "Data recorded, but not printed"
	if output=="S":
		print "Distance of atoms in "+obj+"/"+ref+"/"+aname+" to all atoms within "+dist+" Angstroms"
		if Hbonds=="Y": print "Distances restricted to potential H-bond pairs"
		print screenOP	
	if output=="P":
		if aname=="*": aname="ALL"
		print 'data printed in "distances_rH_'+ref+'-'+aname+'.txt" file'
		f=open('distances_rH_'+ref+'-'+aname+'.txt','w')
		f.write("Pairwise distances betweet atoms in %s and all atoms within %s Angstroms\n" % (obj+"/"+ref+"/"+aname, dist))
		if Hbonds=="Y": f.write("Distances restricted to potential H-bond pairs\n")
		f.write("Atom in reference\tAtom in destination\t\tdistance\n")
		f.write(fileOP)
		f.close()
	print "All done! Good luck with your data"

	#graphical output
	if show=="N": cmd.delete ("dist*")
	if show=="Y":
		cmd.show("lines", "Reference")
		cmd.show("lines", "Residues")
				
cmd.extend("distancesRH", distancesRH);
