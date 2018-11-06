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
    if x=='ORIGIN      \n':
        sequence=''
        x=f.readline()
        while x!="//\n":
            for i in x.strip().split()[1:]:
                sequence+=i
                x=f.readline()
        rawdata.append([sequence])
        x=f.readline()
    x=f.readline()
        
                    
        

