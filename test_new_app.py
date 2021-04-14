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
        self.emp.emp_db = self.fake_emp_db()

    def test_is_id_exist(self):
        self.assertFalse(self.emp.is_id_exist())
        self.assertTrue(self.emp1.is_id_exist())
        self.assertTrue(self.emp.is_id_exist('1'))

    def test_create(self):
        self.assertEqual(self.emp.create(), "Record Created Successfully")
        self.assertRaises(KeyError, self.emp1.create)

    def test_update(self):
        self.assertEqual(self.emp.update('1', 'f_name', 'mary'), "Updated successfully")
        self.assertRaises(KeyError, self.emp1.update, '5', 'f_name', 'mary')
        # with self.assertRaises(ValueError):
        #     self.emp.update('5', 'f_name', 'mary')

    def test_del_rec(self):
        self.assertEqual(self.emp.delete_rec('1'), 'Record deleted')
        self.assertRaises(KeyError, self.emp.delete_rec, '7')


if __name__ == '__main__':
    unittest.main(verbosity=2)
