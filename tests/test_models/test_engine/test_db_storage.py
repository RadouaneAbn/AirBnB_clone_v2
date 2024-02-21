#!/usr/bin/python3
import unittest
from models.engine.db_storage import DBStorage
# from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
# from models.place import Place
# from models.review import Review
# from models.amenity import Amenity


class test_dbstorage(unittest.TestCase):
    """Test db_storage class method """

    def setUp(self):
        self.db_storage = DBStorage()
        self.db_storage.reload()
    
    def tearDown(self):
        del self.db_storage
    
    def test_init(self):
        db_storage = DBStorage()
        self.assertIsNone(db_storage._DBStorage__engine)
        expected_connection_string = 'mysql+mysqldb://user:password@localhost/database'
        self.asserEqual(str(db_storage._DBStorage__engine.url), expected_connection_string)
        self.assertEqual(len(db_storage._DBStorage__engine.table_names()), 0)
    
    def test_reload(self):
        db_storage = DBStorage

        exist_state = State(name='Rabat')
        db_storage._DBStorage__session.add(exist_state)
        db_storage.DBStorage__session.commit()

        db_storage.reload()

        self.assetGreater(len(db_storage._DBStorage__engine.table_names()), 0)

        self.assertEqual(len(db_storage.all(State)), 0)
    def test_new(self):
        state = State(name='Ssouss')
        city = City(name='Agadir', state_id='test_password')
        user = User(userame='test_user', password='test_password')

        self.db_storage.new(state)
        self.db_storage.new(city)
        self.db_storage.new(user)

        self.assertTrue(state in self.db_storage._DBStorage__session)
        self.assertTrue(city in self.db_storage._DBStorage__session)
        self.assertTrue(user in self.db_storage._DBStorage__session)
    
    def test_save(self):
        state = State(name='Elhouz')
        self.db_storage.new(state)
        self.db_storage.save()

        saved_state = self.db_storage.all(State).values()
        self.assertEqual(len(saved_state), 1)
        self.assertEqual(saved_state[0].name, 'Elhouz')
    
    def test_all(self):
        state = State(name='Massa')
        city = City(name='Rachidia',state_id=state.id)
        user =User(username='test_user_2',password='test_password_2')

        self.db_storage.new(state)
        self.db_storage.new(city)
        self.db_storage.new(user)
        self.db_storage.save()

        all_inst = self.db_storage.all()
        self.assertTrue(state in all_inst.values())
        self.assertTrue(city in all_inst.values())
        self.assertTrue(user in all_inst.values())
    
    def test_delete(self):
        state = State(name='Casablanca')
        self.db_storage.new(state)
        self.db_storage.save()

        self.assertTrue(state in self.db_storage._DBStorage__session)

        self.db_storage.delete(state)
        self.db_storage.save()
        self.asserFalse(state in self.db_storage._DBStorage__session)

if __name__ == "__main__":
    unittest.main()
