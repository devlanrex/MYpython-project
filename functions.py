l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
l4=l1.extend(l2)
print(l1)

l1=[1,2,3]
l2=l1.reverse()
print(l1)
print(l2)

def base10_2(m):
    bl=[]
    while(m!=0):
        bl.append(m%2)
        m//2
    bl.reverse()
bv=base10_2(70)
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