#!/usr/bin/env python3
import sys
from Bio import SeqIO
from Bio.Alphabet import generic_dna, generic_protein
from Bio.Blast import NCBIWWW, NCBIXML

sequence = SeqIO.read(sys.argv[1], "fasta")

reshandle = NCBIWWW.qblast("blastn", "nt", sequence.seq)
blast_result = NCBIXML.parse(reshandle)
            
'''
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

def get_seqrecs(alignments, threshold):
    for aln in alignments:
        for hsp in aln.hsps:
            if hsp.expect < threshold:
                yield SeqRecord(Seq(hsp.sbjct), id=aln.accession)
                break

best_seqs = get_seqrecs(blast_result.alignments, 1e-90)
SeqIO.write('blastoutput.fa', 'fasta')
'''
