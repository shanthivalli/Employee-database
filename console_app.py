import json
f1=open("db.json","r")
data=json.load(f1)
emp_db=data
def print_operations():
    print("""Choose any one of the operation
    1.Create new record
    2.Display all the records
    3.Update a record
    4.Delete a record
    5.Exit 
    """)
while True:
    print_operations()
    choice=int(input())
    if choice == 1:
        empId=int(input("Enter empId: "))
        name=input("Enter Name: ")
        age=input("Enter age: ")
        phnNo=input("Enter phnNo: ")
        emp_db.update({empId:{'name':name,'age':age,'phnNo':phnNo}})
    elif choice == 2:
        print(emp_db)
    elif choice == 3:
        id_=input("Enter the id to be updated: ")
        field=input("Enter the field to be updated: ")
        value=input("Enter the value: ")
        if id_ in emp_db:
            emp_db[id_].update({field:value})
        else:
            print("Enter a valid id")
        print("Updated successfully and the updated db is: \n")
        print(emp_db)
    elif choice == 4:
        id_=int(input("Enter the id of the record to be deleted: "))
        emp_db.pop(id_)
        print("Record deleted successfully")
    elif choice == 5:
        print("See you again")
        break
f1 = open("db.json","w")
json.dump(emp_db,f1)
f1.close()