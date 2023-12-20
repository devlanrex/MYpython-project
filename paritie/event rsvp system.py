sit= []
for i in range(1, 11):
    sit.append(i)
attendees= {}
prompt= '''1.register
          2.view attendees
          3.cancel
          4.change sit
          5.exit'''
while True:
    print(prompt)
    option=input()
    if option=='1':
        name = input('Enter your name')
        gender = input('Enter your sex(M/F):')
        print(f'select sit no for the available sit below\n {sit}')
        sit_no = int(input())
        while not (sit.__contains__(sit)):
            print(f'renter the sit no from the available no \n{sit}')
            sit_no= int(input())
        attendee={'name':name,'gender':gender}
        attendees[sit_no]=attendee
        sit.remove(sit_no)
        print(f' registration successful for seat {sit_no}')
    elif option =='2':
        print('attendee in attendees.items ')
        for seat,  attendee in attendees.items():
            print(f"sit {seat} : {attendee['name']} {attendee ['gender']}")
    elif option =='3':
        sit_no =int(input('enter present sit number to cancel:'))
        sit_no_found = False
        for key  in attendees:
            if key == sit_no:
                attendees.pop(key)
                sit.append(key)
                print('reservation cancelled!')
                sit_no_found = True
                break
        if not (sit_no_found):
            print(f'the sit number {sit_no}is not found')
    elif option =='4':
         old_sit_no= int(input('enter your old sit number:'))
         new_sit_no= int(input(f'enter your new sit number from the available below{sit}'))
         while not (sit.__contains__(new_sit_no)):
             new_sit_no=int(input(f'please reenter sit_no{sit}'))
         sit_no_found=False
         for key in attendees:
             if key ==old_sit_no:
                 attendee=attendees[key]
                 attendees.pop(key)
                 attendees[new_sit_no]=attendees
                 sit.append(old_sit_no)
                 print('sit changes successfully')
                 sit_no_found=True
         if not (sit_no_found):
             print(f'the old sit number {old_sit_no} is not found')







