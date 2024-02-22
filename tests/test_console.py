#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import *

class Test_HBNBCommand(unittest.TestCase):
    """test HBNBCommand class"""
    
    def setUp(self):
        self.console = HBNBCommand()
    
    def tearDown(self):
        del self.console
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")
        self.assertEqual(mock_stdout.getvalue(), "")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")
        # self.assertEqual(mock_stdout.getvalue(), "")
    
    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseMOdel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)
    
    def test_do_show(self):
        objects_dict = storage.all("BaseModel")
        if not objects_dict:
            self.fail("No instances of BaseModel found in storage.")

        obj_id = list(objects_dict.keys())[0]

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertTrue(obj_id in storage.all("BaseModel"))
    
    def test_do_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)
    
    def do_cout(self):
        obj_id = list(storage.all("BaseModel").keys())[0]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(f"update BaseModel {obj_id} name 'New Name'")
        self.assertEqual(storage.all("BaseModel")[obj_id].name, 'New Name')

if __name__ == '__main__':
    unittest.main()