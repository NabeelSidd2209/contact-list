contacts={}
from mysql.connector import connection
con=connection.MySQLConnection(host='localhost',user='root',password='2209',database='connectivity')
cur=con.cursor()
q="create table if not exists contacts(name varchar(50),phone varchar(50),email varchar(50),address varchar(50))"
cur.execute(q)
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
        q="insert into contacts(name,phone,email,address) values(%s,%s,%s,%s)"
        val=(name,phone,email,address)
        cur.execute(q,val)
        con.commit()
        print("###Contact Added Successfully###")
    elif choice==2:
        name=input("Enter Name to Delete: ")
        q="delete from contacts where name=%s"
        val=(name,)
        cur.execute(q,val)
        con.commit()
        print("###Contact Deleted###")
    elif choice==3:
        name=input("Enter Name to edit: ")
        phone=input("New Phone: ")
        email=input("New email: ")
        address=input("New address: ")
        q="update contacts set phone=%s,email=%s,address=%s where name=%s"
        val=(phone,email,address,name)
        cur.execute(q,val)
        con.commit()
        print("###Contact Updated###")
    elif choice==4:
        name=input("Enter Name to search: ")
        q="select name,phone,email,address from contacts where name=%s"
        val=(name,)
        cur.execute(q,val)
        data=cur.fetchone()
        if data:
            print("Name: ",data[0])
            print("Phone: ",data[1])
            print("Email: ",data[2])
            print("Address: ",data[3])
        else:
            print("###Contact Not Found###")
    elif choice==5:
        q="select name,phone,email,address from contacts"
        cur.execute(q)
        data=cur.fetchall()
        if len(data)==0:
            print("###No Contact Available###")
        else:
            print("\n====Contact List====")
            for row in data:
                print("Name: ",row[0])
                print("Phone: ",row[1])
                print("Email: ",row[2])
                print("Address: ",row[3])
    elif choice==6:
        break
    else:
        print("###Invalid Choice###")
cur.close()
con.close() 