import re
f=open(r'C:\Users\Alberto\Downloads\sequence1.gb')
rawdata=[]
total=[]
x=f.readline()
while x!='':
    gene=''
    if " mRNA " in x:
        if "join" in x:
            positions=re.findall('\d+', x)
            x=f.readline()
            total.append(positions)
            if '/gene=' in x:
                gene=x.strip().split('/gene=')[1].strip('"')
                #rawdata.append([gene,positions])
                total.append(gene)
                x=f.readline()
            x=f.readline()
        x=f.readline()
    if " CDS " in x:
        if "join" in x:
            cds1=re.findall('\d+', x)
            cds=[cds1[0], cds1[len(cds1)-1]]
            total.append(cds)
            total=[total[1],total[0],total[2]]
            rawdata.append(total)
            total=[]
            x=f.readline()
        x=f.readline()
            
    if 'ORIGIN' in x:
        x=f.readline()
        #sequence=''
        save = open(r'C:\Users\Alberto\Downloads\seq1.txt', 'a')
        #something=0
        
        while "//" not in x:
            #print(something)
            new = x.strip().split()[1:]
            for i in new:
                save.write(i)
                #something+=1
            x=f.readline()  
        save.close()
        x=f.readline()
        
    #rawdata.append([sequence])
    x=f.readline()

#store the rawdata list also
save1= open(r'C:\Users\Alberto\Downloads\rawdata.txt', 'w')
for s in rawdata:
    save1.write(str(s)+"\n")
save1.close()






















    



               
        

