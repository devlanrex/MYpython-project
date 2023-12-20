def base10_16(m):
    bl=[]
    while(m!=0):
        bl.append(m%2)
        m//2
    bl.reverse()
bv=base10_16(70)
for i in bv:
    print(i,end="")

def base10_16(m):
    bl=[]
    while(m!=0):
        bl.append(m%16)
        m//16
    bl.reverse()
    return bl
bv=base10_16(70)
for i in bv:
    print(i,end="")