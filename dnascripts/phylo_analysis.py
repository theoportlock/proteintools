#!/usr/bin/env python3
import sys
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Phylo import PhyloXML
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO
from Bio.Phylo.Applications import PhymlCommandline
from Bio import Phylo
from Bio import SearchIO

'''
turn a distance matrix into a tree with bio phylo treeconstruction
'''
fastafile = "results.fa"
blastxmlfile = "results.xml"
threshold = 1e-90

cmdline = MuscleCommandline(input=fastafile, out='blast.aln', clw=True)
cmdline()

AlignIO.convert(in_file='blast.aln', in_format='clustal',out_file='blast.phy', out_format="phylip-relaxed")
cmdline = PhymlCommandline(input='blast.phy', datatype='nt', model='WAG', alpha='e', bootstrap=100)
ouk_log, err_log = cmdline()

tree = Phylo.read("blast.phy_phyml_tree.txt", "newick")
Phylo.draw_ascii(tree)
Phylo.draw(tree)

def get_seqrecs(alignments, threshold):
    for aln in alignments:
        for hsp in aln.hsps:
            if hsp.expect < threshold:
                yield SeqRecord(Seq(hsp.sbjct), id=aln.accession)
                break

# Promote the basic tree to PhyloXML
phy = tree.as_phyloxml()
blastxml = NCBIXML.read(open(blastxmlfile, "r"))
best_seqs = get_seqrecs(blastxml.alignments, threshold)
SeqIO.write(best_seqs, "best_alignments.fasta", "fasta")

# Make a lookup table for sequences
lookup = dict((rec.id, str(rec.seq)) for rec in best_seqs)
for clade in phy.get_terminals():
    key = clade.name
    accession = PhyloXML.Accession(key, 'NCBI')
    mol_seq = PhyloXML.MolSeq(lookup.get(key), is_aligned=True)
    sequence = PhyloXML.Sequence(type='nt', accession=accession, mol_seq=mol_seq)
    clade.sequences.append(sequence)

# Save the annotated phyloXML file
Phylo.write(phy, 'phylo.xml', 'phyloxml')
