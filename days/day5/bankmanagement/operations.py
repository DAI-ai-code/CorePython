bankdata = {}

def create_account(accid, balance):
    bankdata[accid] = balance
    print(f'Account with ID {accid} and balance = {balance} created successfully')

def deposit(accid, amount):
    bankdata[accid] += amount
    print('Amount added! Now your balance is: {}'.format(bankdata[accid]))

def withdraw(accid, amount):
    bankdata[accid] -= amount
    print('Amount withdrawn! Now your balance is: {}'.format(bankdata[accid]))

def checkbalance(accid):
    print(f'Account with ID {accid} has balance = {bankdata[accid]}')

def transfer_money(senderid, recieverid, amount):
    bankdata[senderid] -= amount
    bankdata[recieverid] += amount
    print('Transfer successfull. Balance of sender: {}'.format(bankdata[senderid]))





