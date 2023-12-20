employees= {100: {'name':'kobi','hr':7},
            101: {'name':'ada','hr':5.2},
            102: {'name':'shola','hr':2},
            103: {'name':'hauwau','hr':100}}
print('s/n\t\tID\t\t\tname\t\t\tsalary')

rate=50
i=1
for key in employees:
    name=employees[key]['name']
    salary=employees[key]['hr']*rate
    print(f'{i}\t\t{key}\t\t\t{name}\t\t\t ${salary}')
    i=i+1