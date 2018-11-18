import ast
rawdata= open(r'C:\Users\Alberto\Downloads\rawdata.txt')
rawdata=rawdata.readlines()

info=[]
for i in rawdata:
    info.append(ast.literal_eval(i.strip("\n")))

seq=open(r'C:\Users\Alberto\Downloads\seq1.txt')
seq=seq.readlines()

int_seq=[]
for x in info:
    guides = [int(i) for i in x[1]]
    results=[x[0],["gene size (nb)",guides[len(guides)-1]- guides[0]+1],["exons number",int(len(guides)/2) ], ["introns number", int((len(guides)/2)-1)]]
    cds=[int(i) for i in x[2]]
    exons=int(len(guides)/2)
    introns= int((len(guides)/2)-1)
    mRNA_n=0
    #mRNA=''
    int_seq1=[]
    int_seq1.append([x[0]])
    mRNA_sep=[]
    for i in range(0,exons):
        results.append(["exon "+str(i+1)+" size (nb)", guides[2*i+1]-guides[2*i]+1])
        mRNA_n+=(guides[2*i+1]-guides[2*i]+1)
        mRNA_sep.append([guides[2*i+1]-guides[2*i]+1])
        #mRNA+=seq[0][(guides[2*i]-1):guides[2*i+1]]
    for i in range (0,introns):#this is for keeping the introns in int_seq object
        int_seq1.append(seq[0][(guides[2*i+2]-2):guides[2*i+3]])

    int_seq.append(int_seq1)
    results.append(["mRNA size (nb)", mRNA_n])
    CDS_size=guides[1]-cds[0]+1,cds[1]-guides[len(guides)-2]+1,mRNA_sep[(len(mRNA_sep)-2)][0]#posible bias if only 1 exon
    #print(CDS_size)
    results.append(["CDS size (nb)",sum(CDS_size)])
    results.append(["5' UTR size", cds[0]-guides[0]])
    results.append(["3' UTR size", guides[len(guides)-1]-cds[1]])
    results.append(["proteine AA size", (sum(CDS_size)-3)/3])#-3 for the stop seq
    
    print(results)


#intron seq alignment
int_seq[0][1][:14]
int_seq[0][2][:14]

#seq1 & seq2 MUST be a list with two str variables to be compared
#compares 15 
def compare (seq1):
    comp=''
    for i in range(0,15):
        if seq1[0][i]==seq1[1][i]:
            comp+=seq1[1][i]
        else:
            comp+='N'
    return(comp)

print("intron-intron of each 5 genes")
for x in int_seq:
    print(compare(x[1:3]))
#print(compare(int_seq[0][1:3]))

print("comparing first introns")
l=1
int_seq.append([0])
int_seq=int_seq[::-1]
for x in range(1,5):
    g1=int_seq[x][l]
    g2=int_seq[:]
    del g2[x]
    indexes=''
    for n in range (1,len(g2)):
        indexes+=g2[n][0][0]+", "
    print(int_seq[x][0][0]+ " against "+ indexes)
    for m in range (1,len(g2)):
        print(compare([g1,g2[m][l]]))


print("comparing second introns")
l=2
for x in range(1,5):
    g1=int_seq[x][l]
    g2=int_seq[:]
    del g2[x]
    indexes=''
    for n in range (1,len(g2)):
        indexes+=g2[n][0][0]+", "
    print(int_seq[x][0][0]+ " against "+ indexes)
    for m in range (1,len(g2)):
        print(compare([g1,g2[m][l]]))



















    #gene=seq[0][(guides[0]-1):guides[len(guides)-1]]


