from Bio import SeqIO
from Bio import Seq
import argparse
import sys
import re

##look for start:end ORF per strand (+1/-1)
def find_orfs(seq):
    answer = []
    for strand, nuc in [(+1, seq), (-1, seq.reverse_complement())]:
        for frame in range(3):
            seq_str = str(seq)
            pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))', re.I)
            match = pattern.findall(seq_str)
            start = match.start()
            end = match.end()
            answer.append(start,end,strand,frame)
    answer.sort()
    return answer

##sepperated output of fasta id, orf length, orf start:stop

orf_list = find_orfs(seq.seq)

for start, end, frame, strand in orf_list:
    print("%s, has ORF on frame %s strand %s, %s:%s" \
            %seq.id, frame, strand, start, end))
