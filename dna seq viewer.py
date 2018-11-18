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






















    



               
        

