import json
f1 = open("db.json", "r")
data = json.load(f1)


class Employee:
    emp_db = data

    def __init__(self, emp_id, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.email = f_name+'.'+l_name+'@company.com'
        self.age = age
        self.emp_id = emp_id

    def is_id_exist(self, _id=None):
        if _id is None and self.emp_id in self.emp_db:
            return True
        elif _id in self.emp_db:
            return True
        else:
            return False

    def create(self):
        if not self.is_id_exist():
            self.emp_db[self.emp_id] = {'f_name': self.f_name,
                                        'l_name': self.l_name,
                                        'email': self.email,
                                        'age': self.age
                                        }
            return "Record Created Successfully"
        return "There exist a record with the id you have entered\n"

    def update(self, _id, field, value):
        if self.is_id_exist(_id):
            self.emp_db[_id].update({field: value})
            return "Updated successfully"
        return "There is no existing record for the specified id\n"

    def delete_rec(self, _id):
        if self.is_id_exist(_id):
            del_rec = self.emp_db.pop(_id)
            print("Deleted record is:", del_rec)
            return 'Record deleted\n'
        return "There is no existing record for the specified id\n"

    def display_rec(self, _id):
        if self.is_id_exist(_id):
            print(self.emp_db.get(_id))
            return "Record Found\n"
        return "There is no existing record for the specified id\n"


def print_operations():
    print("""Choose any one of the operation
    1.Create new record
    2.Display all the records
    3.Update a record
    4.Delete a record
    5.Display a particular record
    6.Exit 
    """)


if __name__ == '__main__':
    while True:
        print_operations()
        choice = int(input())
        e1 = Employee(None, "", "", None)
        if choice == 1:
            emp_id = input("Enter empId: ")
            f_name = input("Enter First Name: ")
            l_name = input("Enter Last Name: ")
            age = input("Enter age: ")
            e1 = Employee(emp_id, f_name, l_name, age)
            print(e1.create())
        elif choice == 2:
            print(Employee.emp_db)
        elif choice == 3:
            _id = input("Enter the id to be updated: \n")
            field = input('''Enter the field to be updated,
                            Firstname: f_name
                            Lastname : l_name
                            Age      : age\n'''
                          )
            value = input("Enter the value: ")
            print(e1.update(_id, field, value))
        elif choice == 4:
            _id = input("Enter the id to be deleted: \n")
            print(e1.delete_rec(_id))
        elif choice == 5:
            _id = input("Enter the id of the required record\n")
            print(e1.display_rec(_id))
        elif choice == 6:
            break
    f1 = open("db.json", "w")
    json.dump(Employee.emp_db, f1)
    f1.close()
