word='coding'
for i in range(2**len(word)):
    bv=''
    j=i
    while j>0:
        bv=str(j%2)+bv
        j=j//2
    if bv=='':
       bv='0'* len(word)
    else:
       pad='0'*(len(word)-len(bv))
       bv=pad+bv
    new_word=''
    c=0
    while c<len(word):
        if bv[c]=='0':
           new_word+=word[c].lower()
        else:
           new_word+=word[c].upper()
        c+=1
    print(new_word)