# gene_mRNA_parser
Pyhton target gene mRNA parser from NCBI nucleotide database

DESCRIPTION
This very simple and basic pyhton code takes a .gb file that can be downloaded from the NCBI nucleotide database and read each line to get the following information in a list:
1. Name of each protein encoded
2. Pair positions of each exon for the mRNA
3. CDS START and STOP positions

Then: it saves the gene sequence in in a file called seq1.txt and the list information in a file called rawdata.txt

# seq_operations
This file takes the input from *gene_mRNA_parser* text documents seq1.txt & rawdata.txt and displays in the console the following information for each gene:
 gene size (nb)	.	.	.	.	.
 Exons number	.	.	.	.	.
 Introns number	.	.	.	.	.
 Exon 1 size (nb)	.	.	.	.	.
 Exon 2 size (nb)	.	.	.	.	.
 Exon 3 size (nb)	.	.	.	.	.
 mRNA size (nb)	.	.	.	.	.
 CDS size (nb)	.	.	.	.	.
 5'UTR size	.	.	.	.	.
 3'UTR size
  
 After that, it prints in the console the information of the following 15 base starting intron sequence comparison :
  + between each gene introns by pairs
  + between each first introns for each gene by pairs
  + between each second introns for each gene by pairs
  
  
LIMITATIONS
Currently, seq alignment is only by pairs.
  
  

PERSPECTIVES
Multiple seq alignment in a more efficient way.
  
  
  
Made for the UGA Epigenetics T course TP.  





