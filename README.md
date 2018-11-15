# gene_mRNA_parser
Pyhton target gene mRNA parser from NCBI nucleotide database

DESCRIPTION
This very simple and basic pyhton code takes a .gb file that can be downloaded from the NCBI nucleotide database and read each line to get the following information in a list:
1. Name of each protein encoded
2. Pair positions of each exon for the mRNA

Then: it saves the gene sequence in *one line*, in a text document called seq1.txt
The last element of the list is the complete DNA sequence
  
  
  
LIMITATIONS
The gene sequence is only one string line of ~86K letters, which crushes the computer 
  
  

PERSPECTIVES
To overcome this limitation I am thinking of mimicking the process of recognition of codons to store the desired sequences, or write a code that stores the sequences of each gene  so they can be processed but consuming less memory.
  
  
  
Made for the UGA Epigenetics T course TP.  





