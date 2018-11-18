import re
f=open(r'C:\Users\Alberto\Downloads\sequence.gb')
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
    x=f.readline()
                    
               
                    
print(rawdata)
