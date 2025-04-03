#!/usr/bin/env python3
import sys
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna, generic_protein
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Phylo import PhyloXML
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO
from Bio.Phylo.Applications import PhymlCommandline
from Bio import Phylo
from Bio import SearchIO

'''
def get_seqrecs(alignments, threshold):
    for aln in alignments:
        for hsp in aln.hsps:
            if hsp.expect < threshold:
                yield SeqRecord(Seq(hsp.sbjct), id=aln.accession)
                break

#sequence = SeqIO.read(sys.argv[1], "fasta")
sequence = SeqIO.read("pET46-nttA/ntta.fasta", "fasta")
reshandle = NCBIWWW.qblast("blastn", "nt", sequence.seq)

with open("blast.xml", 'w') as xml_file:
    xml_file.write(reshandle.readall())

#blast_result = NCBIXML.parse(reshandle)
#results = list(blast_result)


blast_qresult = SearchIO.read("blast.xml", 'blast-xml')
records = []
for hit in blast_qresult:
    records.append(hit[0].hit)
SeqIO.write(records, "blast.faa", "fasta")

with open("blast.faa", "w") as handle:
    for i in results:
        best_seqs = get_seqrecs(i.alignments, 1e-19)
        SeqIO.write(i+best_seqs,handle, 'fasta')
'''

cmdline = MuscleCommandline(input="blast.faa", out='blast.aln', clw=True)
cmdline()
AlignIO.convert(in_file='blast.aln', in_format='clustal',out_file='blast.phy', out_format="phylip-relaxed")
cmdline = PhymlCommandline(input='blast.aln', datatype='aa', model='WAG', alpha='e', bootstrap=100)

ouk_log, err_log = cmdline()
tree = Phylo.read("blast.phy_phyml_tree.txt", "newick")
Phylo.draw_ascii(tree)
# Promote the basic tree to PhyloXML
phy = tree.as_phyloxml()
# Make a lookup table for sequences
lookup = dict((rec.id, str(rec.seq)) for rec in best_seqs)
for clade in egfr_phy.get_terminals():
    key = clade.name
    accession = PhyloXML.Accession(key, 'NCBI')
    mol_seq = PhyloXML.MolSeq(lookup[key], is_aligned=True)
    sequence = PhyloXML.Sequence(type='aa', accession=accession, mol_seq=mol_seq)
    clade.sequences.append(sequence)

# Save the annotated phyloXML file
Phylo.write(egfr_phy, 'egfr-family-annotated.xml', 'phyloxml')
