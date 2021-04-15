import unittest
import new_app


class ConsoleAppTest(unittest.TestCase):
    @staticmethod
    def fake_emp_db():
        return {'1':   {"f_name": "shanthi",
                        "l_name": "arumugam",
                        "email": "shanthi.arumugam@company.com",
                        "age": "21"
                        },
                '2':   {"f_name": "siva",
                        "l_name": "arumugam",
                        "email": "siva.arumugam@company.com",
                        "age": "19"
                        }
                }

    def setUp(self):
        self.emp = new_app.Employee('3', 'teddy', 'bear', '25')
        self.emp1 = new_app.Employee('2', 'teddy', 'bear', '25')
        self.temp = new_app.Employee.emp_db
        new_app.Employee.emp_db = self.fake_emp_db()

    def test_is_id_exist(self):
        self.assertFalse(self.emp.is_id_exist())
        self.assertTrue(self.emp1.is_id_exist())
        self.assertTrue(self.emp.is_id_exist('2'))

    def test_create(self):
        self.assertEqual(self.emp.create(), "Record Created Successfully")
        self.assertEqual(self.emp1.create(), "There exist a record with the id you have entered\n")

    def test_update(self):
        self.assertEqual(self.emp.update('1', 'f_name', 'mary'), "Updated successfully")
        self.assertEqual(self.emp1.update('5', 'f_name', 'mary'), "There is no existing record for the specified id\n")

    def test_del_rec(self):
        self.assertEqual(self.emp.delete_rec('1'), 'Record deleted\n')
        self.assertEqual(self.emp.delete_rec('7'), "There is no existing record for the specified id\n")

    def test_display_rec(self):
        self.assertEqual(self.emp.display_rec('1'), "Record Found\n")
        self.assertEqual(self.emp.display_rec('3'), "There is no existing record for the specified id\n")

    def tearDown(self):
        new_app.Employee.emp_db = self.temp


if __name__ == '__main__':
    unittest.main(verbosity=2)
