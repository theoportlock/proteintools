#!/usr/bin/env python3
import pandas as pd
from pydna.genbank import Genbank
from pydna.dseqrecord import Dseqrecord

df = pd.read_csv('Primers.csv')
df1 = df[["Name","Complete sequence"]]

'''
from Bio import Entrez
Entrez.email = "zn.tportlock@gmail.com"
ID = "NC_002942.5"
handle = Entrez.efetch(db="nucleotide", id=ID, rettype="fasta", retmode="fasta")
with open("genome.fasta","w") as file:
    file.write(handle.read())
'''

gb = Genbank("zn.tportlock@gmail.com")
lgenome = gb.nucleotide("NC_002942.5")
ntta = gb.nucleotide("LN901282")
nttaprot = ntta.translate(table=15,to_stop=True)

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein
myntta = Seq("MAHHHHHHVDDDDKMEDTANPNEMTKDAWLNSMTPLLPDLICKGFIQDPDLKKRFDEIKMTYEQCVTLIPESTKKCQDELYASMPDKINSETAGTWGRSLGECIGKDFAEKHLIPK", generic_protein)

from Bio.Blast import NCBIWWW, NCBIXML
reshandle = NCBIWWW.qblast("blastn", "nt", ntta.seq)

blast_result = NCBIXML.parse(reshandle)
            
for b in blast_result:
    for alignment in b.alignments:
        for hsp in alignment.hsps:
            print('Align')
            print('Sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')
            print("")
