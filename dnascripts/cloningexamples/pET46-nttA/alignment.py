import pandas as pd
from pydna.genbank import Genbank
from pydna.dseq import Dseq
from pydna.dseqrecord import Dseqrecord
from pydna import amplify
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Restriction import Restriction
from Bio import pairwise2
from Bio.Alphabet import generic_dna, generic_protein

genome = SeqIO.read("lgenome.fasta", "fasta")
protein_seq = SeqIO.read("ntta.fasta", "fasta")

alignments = pairwise2.align.globalxx(str(protein_seq.seq), str(genome.seq[:]))

print(alignments[0])
