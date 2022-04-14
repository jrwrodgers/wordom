from itertools import combinations

def bit_patterns(size, ones):
    for pos in map(set, combinations(range(size), ones)):
        yield [int(i in pos) for i in range(size)]

def replace_twos(b):
    out =[2 if x == 1 else x for x in b]
    # out=[]
    # for el in b:
    #     print("checking el",el)
    #     if el==1:
    #         out.append(2)
    #     else:
    #         out.append(el)
    return out


mm=[]
for i in range(2):
    mat_5=[]
    mat_5=list(bit_patterns(5,i))
    for el in mat_5:
        mm.append(el)
#print(*mm,sep='\n')

mm2=[]
out=[]
for el in mm:
    out=replace_twos(el)
    mm2.append(out)
print(*mm2,sep='\n')
print(len(mm2))


mm4=[]
for el in mm2:
    mm3 = []
    seq=el.count(0)
    for i in range(seq+1):
        mat = []
        mat = list(bit_patterns(seq, i))
        for el in mat:
            mm3.append(el)
    seq2=len(mm3)
    print(*mm3, sep='\n')
    print(seq2)


    #for ll in el:


