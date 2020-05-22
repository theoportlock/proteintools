from Bio.Blast import NBCIStandalone, NCBIXML
from Bio.Phylo import PhyloXML
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO
from Bio.Phylo.Applications import PhymlCommandline
from Bio import Phylo
import sys

# First argument being the fasta
query_fname = sys.argv[1]
result_handle, error_handle = NCBIStandalone.blastall('/usr/bin/blastall', 'blastp',
blast_record = NCBIXML.read(result_handle)

def get_seqrecs(alignments, threshold):
    for aln in alignments:
        for hsp in aln.hsps:
            if hsp.expect < threshold:
                yield SeqRecord(Seq(hsp.sbjct), id=aln.accession)
                break

best_seqs = get_seqrecs(blast_record.alignments, 1e-90)
SeqIO.write(best_seqs,'blasted_' + query_fname, 'fasta')
cmdline = MuscleCommandline(input='blasted_' + query_fname, out='blasted_' + query_fname + '.aln', clw=True)
cmdline()
AlignIO.convert('blasted_' + query_fname + '.aln', "clustal",'blasted_' + query_fname + '.phy', "phylip-relaxed")
cmdline = PhymlCommandline(input='blasted_' + query_fname + '.phy', datatype='aa', model='WAG', alpha='e', bootstrap=100)
ouk_log, err_log = cmdline()

egfr_tree = Phylo.read("egfr-family.phy_phyml_tree.txt", "newick")
Phylo.draw_ascii(egfr_tree)
# Promote the basic tree to PhyloXML
egfr_phy = egfr_tree.as_phyloxml()
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
