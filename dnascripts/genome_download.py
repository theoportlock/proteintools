# Imports
from Bio import Entrez
from Bio import SeqIO

#############################
# Retrieve NCBI Data Online #
#############################

Entrez.email     = "zn.tportlock@gmail.com"             # Always tell NCBI who you are
genomeAccessions = ['NC_000913', 'NC_002695', 'NC_011750', 'NC_011751', 'NC_017634', 'NC_018658']
search           = " ".join(genomeAccessions)
handle           = Entrez.read(Entrez.esearch(db="nucleotide", term=search, retmode="xml"))
genomeIds        = handle['IdList']
records          = Entrez.efetch(db="nucleotide", id=genomeIds, rettype="gb", retmode="text")

###############################
# Generate Genome Fasta files #
###############################

sequences   = []  # store your sequences in a list
headers     = []  # store genome names in a list (db_xref ids)

for i,record in enumerate(records):

    file_out = open("genBankRecord_"+str(i)+".gb", "w")    # store each genomes .gb in separate files
    file_out.write(record)
    file_out.close()

    genomeGenbank  = SeqIO.read("genBankRecord_"+str(i)+".gb", "genbank")  # parse in the genbank files
    header         = genome.features[0].qualifiers['db_xref'][0]          # name the genome using db_xfred ID
    sequence       = genome.seq.tostring()                                # obtain genome sequence

    headers.append('>'+header)  # store genome name in list                                     
    sequences.append(sequence)  # store sequence in list

    fasta_out = open("genome"+str(i)+".fasta","w")     # store each genomes .fasta in separate files
    fasta_out.write(header)    # >header ... followed by:
    fasta_out.write(sequence)  # sequence ... 
    fasta_out.close()          # close that .fasta file and move on to next genome
records.close()
