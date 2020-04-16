#!/usr/bin/env python3
from Bio import SeqIO
from Bio.Alphabet import generic_dna, generic_protein
from Bio.Blast import NCBIWWW, NCBIXML

ntta = SeqIO.read("ntta.fasta", "fasta")

myntta = Seq("MAHHHHHHVDDDDKMEDTANPNEMTKDAWLNSMTPLLPDLICKGFIQDPDLKKRFDEIKMTYEQCVTLIPESTKKCQDELYASMPDKINSETAGTWGRSLGECIGKDFAEKHLIPK", generic_protein)

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
