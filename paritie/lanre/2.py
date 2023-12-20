l=[3,4,7,3,3,3,101]
sorted=[]
for item in l:
    if len(sorted)==0:
        sorted.append(item)
        continue
    i=0
    while i<len(sorted):
          if item<sorted[i]:
                sorted.insert(i,item)
                break
          i+=1
    if i ==len(sorted):
     sorted.append(item)
if len(sorted)% 2 !=0:
    median=(len(sorted)-1)/2
    print(median)
else:
         i=(len(sorted)-1//2)
         j=i=1
         median=(sorted[i]+sorted[j])/2
         print(median)