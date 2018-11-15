import re
f=open(r'C:\Users\Alberto\Downloads\sequence.gb')
rawdata=[]
x=f.readline()
while x!='':
    gene=''
    if " mRNA " in x:
        if "join" in x:
            positions=re.findall('\d+', x)
            x=f.readline()
            if '/gene=' in x:
                gene=x.strip().split('/gene=')[1].strip('"')
                rawdata.append([gene,positions])
                x=f.readline()
    if 'ORIGIN' in x:
        sequence=''
        x=f.readline()
        save = open(r'C:\Users\Alberto\Downloads\seq1.txt', 'a')
        while "//" not in x:
            new = x.strip().split()[1:]
            for i in new:
                save.write(i)
        save.close()
        rawdata.append([sequence])
        x=f.readline()
    x=f.readline()
               
        

