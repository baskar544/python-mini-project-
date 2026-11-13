contact={}
while True:
    print("1.add contacts:")
    print("2.search contacts")
    print("3.update contacts")
    print("4.delete contacts")
    print("5.display contacts")
    print("6.exit")
    choice=int(input("enter the choice"))
    if choice==1:
        name=input("enter the name:")
        phone=int(input("enter the phone number:"))
        email=input("enter the email:")
        contact[name]=[phone,email]
        print("contact added")

    elif choice==2:
        name=input("enter the name:")
        if name in contact:
            print(contact[name])
        else:
            print("contacts not found")

    elif choice==3:
        name=input("enter the name")
        if name in contact:
            phone=int(input("enter new phone:"))
            email=input("enter new email")
            contact[name]=[phone,email]
            print("contacts updated")
        else:
            print("contacts not found")

    elif choice==4:
        name=input("enter the name:")
        if name in contact:
            del contact[name]
            print("contacts deleted")
        else:
            print("contacts not found")

    elif choice==5:
        for name in sorted(contact):
            print(name,contact[name])

    elif choice==6:
        break
    else:
        print("invalid choice")
