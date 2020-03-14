names = open('Names.txt')
bodys = open('Body.txt')
Bodys = []
Names = []
for i  in names:
    Names.append(i.rstrip('\n'))
for i  in bodys:
    Bodys.append(i.rstrip('\n'))
for k in range(0,len(Names)):
    f= open(""+Names[k]+".txt","a+")
    f.write("Hello "+Names[k]+',\n\t'+Bodys[k]+'.\n')
bodys.close()
names.close()
f.close()
