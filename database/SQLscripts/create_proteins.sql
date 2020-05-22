CREATE TABLE proteins ( 
	Protein_ID INT NOT NULL AUTO_INCREMENT, 
	Protein_name VARCHAR(20), 
	Protein_ref VARCHAR(20), 
	Plasmid_ID INT NOT NULL, 
	Plasmid_dna_sequence VARCVARBINARY(MAX), 
	PRIMARY KEY (protein_number)
	FOREIGN KEY (Plasmid_ID) REFERENCES plasmids(Plasmid_ID) );
