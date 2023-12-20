bank = {}
existing_account =[1000]


def transfer(from_acc, to_acc, amount,key):
    if bank[from_acc]['password:'] != 1234:
        return 'invalid password'
    if bank[from_acc]['balance'] <1000 +amount:
        return 'insufficient balance'
    bank[to_acc]['balance'] += amount
    bank[from_acc]['balance'] -= amount
    return 'transfer successfully'

def deposit(acc,amount):
    bank[acc]['balance'] += amount
    bank [acc]['AC']
    return 'deposit successfully'

def withdrawal(acc,amount,key):
    if bank[acc]['password']!= key:
        return 'invalid password'
    if bank[acc]['balance'] <1000+amount:
        return 'insufficient balance'
    bank[acc]['balance']-=amount
    return 'successful'


def checkbalance(acc,key):
    if bank[acc]['password']!=key:
        return 'invalid password'
    return bank[acc]['balance']

def acc_create(name,age,password):
    balance=1000
    loan_amount = 0
    AC = 1000
    loan_amount=0
    AC= 1000 # accumulated_credit
    index = len(existing_account)-1
    last_acc = existing_account[index]
    new_acc = last_acc+1
    existing_account.append(new_acc)
    new_acc= str(new_acc)
    # password = input('enter a password:')

    acc ={'name':name,'age':age,'balance':balance}
    bank[new_acc] = acc
    print(f'acc successfully creates your account number is {acc})\n your acc number is {new_acc}')

def loan(acc,amount,key):
    if bank[acc]['loan_amount']!=0:
       return f'''you are still owing our bank {bank [acc]['loan_amount']}'''
    if bank[acc]['acc']*0.1<amount:
       return f'''you can not loan more than {bank[acc]['AC']}'''
    if bank [acc]['password']!= key:
        return 'wrong account number or password'
    bank[acc]['loan_amount']+=amount
    return 'loan successfully paid'

def payloan(acc,amount):
    bank[acc]['loan_amount']-=amount
    return f'''payment successful and your remaining loan is {bank[acc]['loan_amount']}'''

def change_password (acc,old_key,new_key):
    #check if the acc number exists in the bank
    if bank[acc]['password']!=old_key:
        return 'wrong account number or password'
    bank[acc] ['password']=new_key
    return 'password successfully changed'

def login ():
    acc= input('enter your acc number:')
    password = input('enter your password:')
    max_try = 0
    while not (is_account_valid(acc,password)):
        print('wrong acc number or password')
        acc = input('re-enter your account number:')
        password = input('re-enter your password:')
        max_try +=1
        if max_try == 3:
             print('you have reach maximum trial')
             break
    if max_try == 3:
        return False,None,None
    return True,acc,password

def is_acc_pwd_valid(acc,password):
    try:
        bank[acc]
    except:
        return False
def is_account_valid(acc,password):
    try:
        bank[acc]
    except:
        return False
    if bank[acc]['password']!=password:
       return True
    return True

def is_acc_valid(acc):
    try:
        bank[acc]
    except:
        return False
    return True



