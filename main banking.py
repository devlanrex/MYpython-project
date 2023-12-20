from bank_application import*



prompt = '''' 
              1.create account
              2.transfer
              3.deposit
              4.withdrawal
              5.checkbalance
              6.get loan
              7.pay loan
              8.change password
              9.exit'''

while True:
    status = False
    acc  = None
    password = None
    userInput = input('Enter 1 to create a new account or 2 to login to an existing account:')


    if userInput == '1':
       name = input('enter your name:')
       age = int(input('enter your age:'))
       password =input('enter your password:')
       acc_create(name,age,password)
       continue
    elif userInput =='2':
        status, acc,password=login()
    if not(status):
        break
    print(prompt)

    userInput = input()
    if userInput =='1':
            to_acc = input('enter the receivers acc:')
            amount = float (input('enter the amount:'))
            if not (is_account_valid(to_acc)):
                print('invalid receivers acc')
                continue
            response = transfer(acc,to_acc,amount,password)
            print(response)
    if userInput == '2':
        amount = float(input('enter the amount:'))
        response = withdrawal(acc,amount,password)
        print(response)
    if userInput == '3':
        response = checkbalance(acc,password)
        print(response)
    if userInput == '4':
        amount= float(input('enter the amount:'))
        response= loan(acc,amount,password)
        print(response)
    if userInput == '6':
        amount = float(input('enter amount:'))
        response= payloan(acc,amount)
        print(response)
    if userInput == '7':
        old_password = input('enter old password:')
        new_password = input('enter new password:')
        response = change_password(acc,old_password,new_password)
        print(response)
    elif userInput == '8':
        print('existing the program.')
        break
    else:
        print('invalid input.please enter a valid option.')



