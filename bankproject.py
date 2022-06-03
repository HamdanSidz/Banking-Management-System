print()
print("         Banking Management System")
print()
print("Enter operation type number: ")


d = {}
list1 = []
list2 = ['Name ', 'Phone no ', 'Address ', 'Amount ']


def account_creation():
    accnum = int(input("enter account number "))
    for i in range(len(list2)):
        b = input(list2[i])
        list1.append(b)
    d[accnum] = dict(zip(list2, list1))
    print("    Your account is created")
    print("Thanks for account creation into our bank ")


def othermethod(accnum):
    print("1.To Show", "2.To Deposit", "3.To Credit")
    c = int(input("enter choice to continue operation: "))
    if c == 1:
        print(d[accnum])
    elif c == 2:
        new = int(input("Enter amount for deposition "))
        new_amount = int(d[accnum]['Amount ']) + new
        d[accnum]['Amount '] = new_amount
        print("Your new balance is:", d[accnum]['Amount '])
    elif c == 3:
        new = int(input("enter amount for credit "))
        new_amount = int(d[accnum]['Amount ']) - new
        d[accnum]['Amount '] = new_amount
        print("Your remaning balance is:", d[accnum]['Amount '])


def delaccount(accnum):
    del d[accnum]
    a = 0
    for i in d:
        a = a+1
    print("    Updated data base     ")
    print(f"total account left : {a}")


def info():
    a = 0
    for i in d:
        a = a+1
    print()
    print("   Exiting data of accounts    ")
    print(f"total account: {a}")
    print(d)
    print()


forend = "true"
while forend == "true":
    list1 = []
    list2 = ['Name ', 'Phone no ', 'Address ', 'Amount ']

    a = int(
        input("1.For New Coustomer 2.For Exiting Coustomer 3.For Deletion of Account 4.No of account available\n"))
    if a == 1:
        account_creation()
    elif a == 2:
        accnum = int(input("enter account number "))
        if accnum in d:
            print("Account found")
            othermethod(accnum)
        else:
            print("Sorry! your account is not found")
    elif a == 3:
        accnum = int(
            input("enter account number that you are loking for deletion\n"))
        if accnum in d:
            print("    Account found")
            print()
        else:
            print("    Sorry! your account is not found")
        delaccount(accnum)
        print()

    elif a == 4:
        info()

    forend = input("enter True or False to continue or end the program: ")
    if forend == "false":
        break
