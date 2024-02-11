#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestUser(unittest.TestCase):

    """Test Cases for the User class."""

    def setUp(self):
        """Set up test methods."""
        pass

    def tearDown(self):
        """Tear down test methods."""
        self.reset_storage()

    def reset_storage(self):
        """Reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Test instantiation of User class."""
        instance = User()
        self.assertEqual(str(type(instance)), "<class 'models.user.User'>")
        self.assertIsInstance(instance, User)
        self.assertTrue(issubclass(type(instance), BaseModel))

    def test_8_attributes(self):
        """Test the attributes of User class."""
        attributes = storage.attributes()["User"]
        instance = User()
        for key, value in attributes.items():
            self.assertTrue(hasattr(instance, key))
            self.assertEqual(type(getattr(instance, key, None)), value)

if __name__ == "__main__":
    unittest.main()

