import ast
rawdata= open(r'C:\Users\Alberto\Downloads\rawdata.txt')
rawdata=rawdata.readlines()

info=[]
for i in rawdata:
    info.append(ast.literal_eval(i.strip("\n")))

seq=open(r'C:\Users\Alberto\Downloads\seq1.txt')
seq=seq.readlines()

final_results=[]
int_seq=[]
whole_seq=[]
CDSs=[]
for x in info:
    guides = [int(i) for i in x[1]]
    results=[x[0],["gene size (nb)",guides[len(guides)-1]- guides[0]+1],["exons number",int(len(guides)/2) ], ["introns number", int((len(guides)/2)-1)]]
    cds=[int(i) for i in x[2]]
    CDSs1=[]
    CDSs1.append([x[0]])
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

    whole_seq.append(seq[0][guides[5]:guides[0]])


    int_seq.append(int_seq1)

    CDSs1.append(seq[0][(cds[0]-1):(guides[1]-1)])
    CDSs1.append(seq[0][(guides[2]-1):(guides[3]-1)])
    CDSs1.append(seq[0][(cds[1]-1):(guides[5]-1)])
    CDSs.append(CDSs1)
    
    results.append(["mRNA size (nb)", mRNA_n])
    CDS_size=guides[1]-cds[0]+1,cds[1]-guides[len(guides)-2]+1,mRNA_sep[(len(mRNA_sep)-2)][0]#posible bias if only 1 exon
    #print(CDS_size)
    results.append(["CDS size (nb)",sum(CDS_size)])
    results.append(["5' UTR size", cds[0]-guides[0]])
    results.append(["3' UTR size", guides[len(guides)-1]-cds[1]])
    results.append(["proteine AA size", (sum(CDS_size)-3)/3])#-3 for the stop seq
    
    print(results)
    final_results.append(results)


#intron seq alignment
int_seq[0][1][:14]
int_seq[0][2][:14]

#seq1 & seq2 MUST be a list with two str variables to be compared
#compares 15
print("First 15 nt pair analysis")
def compare1 (seq1):
    comp=''
    for i in range(0,50):
        if seq1[0][i]==seq1[1][i]:
            comp+=seq1[1][i]
        else:
            comp+='N'
    return(comp,str(comp.count('N')/50))


for x in int_seq:
    print(x[0],compare1(x[1:3]))
print("Last 15 nt pair analysis")  
#print(compare(int_seq[0][1:3]))
def compare (seq1):
    comp=''
    for i in range(0,15):
        if seq1[0][len(seq1[0])+i-16]==seq1[1][len(seq1[1])+i-16]:
            comp+=seq1[1][i]
        else:
            comp+='N'
    return(comp)

for x in int_seq:
    print(x[0],compare(x[1:3]))
#print(compare(int_seq[0][1:3]))

print ("First 15 nt")
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
        indexes+=str(g2[n][0][0])+", "
    print(int_seq[x][0][0]+ " against "+ indexes)
    for m in range (1,len(g2)):
        print(compare1([g1,g2[m][l]]))


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
        print(compare1([g1,g2[m][l]]))


print("Last 15 nt")
print("comparing first introns")
l=1
int_seq.append([0])
int_seq=int_seq[::-1]
for x in range(1,5):
    g1=int_seq[x][l]
    g2=int_seq[:]
    del g2[x]
    indexes=''
    for n in range (1,len(g2)-1):
        #print(indexes)
        indexes+= str(g2[n][0][0]) +", "
    print(int_seq[x][0][0]+ " against "+ indexes)
    for m in range (1,len(g2)-1):
        print(compare([g1,g2[m][l]]))


print("comparing second introns")
l=2
for x in range(1,5):
    g1=int_seq[x][l]
    g2=int_seq[:]
    del g2[x]
    indexes=''
    for n in range (1,len(g2)-1):
        indexes+=str(g2[n][0][0])+", "
    print(int_seq[x][0][0]+ " against "+ indexes)
    for m in range (1,len(g2)-1):
        print(compare([g1,g2[m][l]]))





save1= open(r'C:\Users\Alberto\Downloads\results.txt', 'w')
save1.write(str(final_results)+"\n")
save1.close()

#int_seq

save2= open(r'C:\Users\Alberto\Downloads\seqalfa.txt', 'w')
save2.write(str(int_seq)+"\n")
save2.close()

save3= open(r'C:\Users\Alberto\Downloads\wholseq.txt', 'w')
save3.write(str(whole_seq)+"\n")
save3.close()

save4= open(r'C:\Users\Alberto\Downloads\cds.txt', 'w')
save4.write(str(CDSs)+"\n")
save4.close()












    #gene=seq[0][(guides[0]-1):guides[len(guides)-1]]


