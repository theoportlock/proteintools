import sys
from Bio import SeqIO
from Bio import Seq

record = SeqIO.read(open(sys.argv[1]), "fasta")
readingframes = [Seq.translate(record.seq[i:], table='Standard', stop_symbol='*', to_stop=False, cds=False) for i in range(3)]

results = []
for frame in readingframes:
    for peptide in frame.split('*'): #Split translation over stopcodons
        if len(peptide[peptide.find("M"):]) > 100:
            results.append(peptide[peptide.find("M"):])

for i in results:
    print(i)

'''
record = SeqIO.read(open(sys.argv[1]), "fasta")
readingframes = [Seq.translate(record.seq[i:], table='Standard', stop_symbol='*', to_stop=False, cds=False) for i in range(3)]

results = []
for frame in readingframes:
    for peptide in frame.split('*'): #Split translation over stopcodons
        if len(peptide) > 100:
            results.append(peptide)

with open('PotentialORFs.txt', 'w') as output: 
    for peptide in results:
        output.write("{}\t{}\n".format(len(peptide), peptide))
'''
