import ast
rawdata= open(r'C:\Users\Alberto\Downloads\rawdata.txt')
rawdata=rawdata.readlines()

info=[]
for i in rawdata:
    info.append(ast.literal_eval(i.strip("\n")))

seq=open(r'C:\Users\Alberto\Downloads\seq1.txt')
seq=seq.readlines()



for x in info:
    guides = [int(i) for i in x[1]]
    results=[x[0],["gene size (nb)",guides[len(guides)-1]- guides[0]+1],["exons number",int(len(guides)/2) ], ["introns number",int(len((guides)/2)-1)]]
    exons=int(len(guides)/2)
    mRNA=0
    for i in range(0,exons):
        results.append(["exon "+str(i+1)+" size (nb)", guides[i+1]-guides[i]+1])
        mRNA+=guides[i+1]-guides[i]+1
    results.append(["mRNA size (nb)", mRNA])
    print(results)
    gene=seq[0][(guides[0]-1):(guides[len(guides)-1]-1)]
    #position of the start codon
    #does not need a +1 because it will need a -1 the "a" position so -1+1=0
    
    start=gene.find("atg")
    stops = ["tta","tga","tag"]
    gene.find(stops)


