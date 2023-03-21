CREATE TABLE plasmids ( 
	Plasmid_ID INT NOT NULL AUTO_INCREMENT, 
	Plasmid_name VARCHAR(20), 
	Plasmid_sequence VARCVARBINARY(MAX), 
	PRIMARY KEY (Plasmid_ID) );
