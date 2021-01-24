#!/usr/bin/env python
from Bio import SearchIO, SeqIO
import sys

def converter(filename):
    blast_qresult = SearchIO.read(filename, 'blast-xml')
    records = []
    for hit in blast_qresult:
        records.append(hit[0].hit)
    return records

if __name__ == "__main__":
    converted = converter(sys.argv[1])
    SeqIO.write(records, sys.argv[1] + ".fa", "fasta")
