#!/usr/bin/env python3
from pydna.dseq import Dseq
from Bio import SeqIO
from Bio.Restriction import Restriction
from Bio.Alphabet import generic_dna, generic_protein
from Bio.

record = SeqIO.read("pet28b.fasta", "fasta", generic_dna)
plasseq = Dseq(str(record.seq),circular=True)
#plascutup = plasseq.cut(Restriction.NcoI,Restriction.KpnI)
