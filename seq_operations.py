import json
rawdata= open(r'C:\Users\Alberto\Downloads\rawdata.txt')
rawdata=rawdata.readlines()
print(rawdata)

seq=open(r'C:\Users\Alberto\Downloads\seq1.txt')
seq=seq.readlines()
for i in range(len(rawdata)):
    in_pos=rawdata[i][1][0]
    fin_pos=rawdata[i][1][len(rawdata[i][1])]
    gene_seq=seq[0][in_pos:fin_pos]
    print(rawdata[i][0],gene_seq)
