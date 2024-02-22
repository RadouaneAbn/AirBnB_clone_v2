#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
# from models.base_model import BaseModel
from models import storage
from os import environ
from models.state import State
# from models.city import City
# from models.user import User
# from models.place import Place
# from models.review import Review
# from models.amenity import Amenity


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 'Test only for DBStorage')
class test_dbStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @classmethod
    def setUpClass(cls):
        """ Set up test environment """
        environ['HBNB_MYSQL_USER'] = 'your_mysql_user'
        environ['HBNB_MYSQL_PWD'] = 'your_mysql_password'
        environ['HBNB_MYSQL_HOST'] = 'your_mysql_host'
        environ['HBNB_MYSQL_DB'] = 'your_mysql_db'
        environ['HBNB_ENV'] = 'test'

    @classmethod
    def tearDownClass(cls):
        """ Remove environment variables after tests """
        del environ['HBNB_MYSQL_USER']
        del environ['HBNB_MYSQL_PWD']
        del environ['HBNB_MYSQL_HOST']
        del environ['HBNB_MYSQL_DB']
        del environ['HBNB_ENV']

    def setUp(self):
        """ Reload the storage engine """
        storage.reload()

    def tearDown(self):
        """ Remove storage file at end of tests """
        storage._DBStorage__session.close()
        storage._DBStorage__engine.dispose()

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = State(name="California")
        storage.new(new)
        storage.save()
        self.assertIn(new, storage.all().values())

    def test_all(self):
        """ __objects is properly returned """
        new_state = State(name="California")
        storage.new(new_state)
        storage.save()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(new_state, all_objs.values())

    def test_save(self):
        """ Save method updates the JSON file """
        new_state = State(name="California")
        storage.new(new_state)
        storage.save()
        storage.reload()
        self.assertIn(new_state, storage.all().values())

    def test_delete(self):
        """ Delete method deletes an object from storage """
        new_state = State(name="California")
        storage.new(new_state)
        storage.save()
        storage.delete(new_state)
        storage.reload()
        self.assertNotIn(new_state, storage.all().values())


if __name__ == "__main__":
    unittest.main()
