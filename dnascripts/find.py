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

genome = SeqIO.read("philadelphiagenome.fasta", "fasta")
protein = SeqIO.read("test.fasta", "fasta")

print(genome.seq.find(str(protein.seq)))
