climate={1:{'T':32,'P':28.1},
         2:{'T':29,'P':26},
         3:{'T':-4,'P':26.7},
         4:{'T':37,'P':32.9},
         5:{'T':20,'P':56.8}}
mt=climate [1]['T']
mp=climate[1]['P']

sumt=0
sump=0
for key in climate:
    sump+=climate[key]['P']
    sumt+=climate[key]['T']
    if mt<climate [key] ['T']:
        mt=climate  [key] ['T']
    if mp<climate [key] ['P']:
        mp=climate [key] ['P']
Avt=sumt/len(climate)
Avp=sump/len(climate)
print(f'Avt is {Avt} and Avp is {Avp} mt is {mt} and mp is {mp}')

