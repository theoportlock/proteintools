CREATE TABLE proteins ( 
	protein_number INT NOT NULL AUTO_INCREMENT, 
	prot_name VARCHAR(20), 
	amino_acid_sequence VARCVARBINARY(MAX), 
	plasmid_dna_sequence VARCVARBINARY(MAX), 
	PRIMARY KEY (protein_number) );
