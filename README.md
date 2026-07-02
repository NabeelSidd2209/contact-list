contacts={}
username=input("Enter Username: ")
password=input("Enter Password: ")

if username=="admin" and password=="1234":
    while True:
        print("\n=====CONTACT MANAGEMENT SYSTEM====")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Edit Contact")
        print("4. Search Contact")
        print("5. List All Contacts")
        print("6. Exit")
        
        choice=int(input("Enter your choice: "))
        
        if choice==1:
            name=input("Enter name: ")
            phone=input("Enter phone: ")
            email=input("Enter email: ")
            address=input("Enter address: ")
            
            contacts[name]={
                "phone":phone,
                "email":email,
                "address":address,
            }
            print("###Contact Added Successfully###")
            
        elif choice==2:
            name=input("Enter Name to Delete: ")
            if name in contacts:
                del contacts[name]
                print("###Contact Deleted###")
            else:
                print("###Contact Not Found###")
        
        elif choice==3:
            name=input("Enter Name to edit: ")
            if name in contacts:
                contacts[name]["phone"]=input("New Phone: ")
                contacts[name]["email"]=input("New email: ")
                contacts[name]["address"]=input("New address: ")
                print("###Contact Updated###")
            else:
                print("###Contact Not Found###")
        
        elif choice==4:
            name=input("Enter Name to search: ")
            if name in contacts:
                contacts[name][phone]=input("Enter Name or Phone:")
                print("###contact Found###")
            else:
                print("###Contact Not Found###")
        
        elif choice==5:
            if len(contacts)==0:
                print("###No Contact Available###")
            else:
                print("\n====Contact List====")
                for name,details in contacts.items():
                    print("Name: ",name)
                    print("Phone: ",details["phone"])
                    print("email: ",details["email"])
                    print("address: ",details["address"])
                    print("-"*30)
        
        elif choice==6:
            print("_"*10,"Thank You!","_"*10)
            break 
        else:
            print("***INVALID CHOICE***") 
        
else:
    print("_",*10,*"**INVALID USERNAME OR PASSWORD***","_"*10)
