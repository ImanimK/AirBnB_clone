#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

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
        """Test instantiation of City class."""
        instance = City()
        self.assertEqual(str(type(instance)), "<class 'models.city.City'>")
        self.assertIsInstance(instance, City)
        self.assertTrue(issubclass(type(instance), BaseModel))

    def test_8_attributes(self):
        """Test the attributes of City class."""
        attributes = storage.attributes()["City"]
        instance = City()
        for key, value in attributes.items():
            self.assertTrue(hasattr(instance, key))
            self.assertEqual(type(getattr(instance, key, None)), value)

if __name__ == "__main__":
    unittest.main()

