#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):

    """Test Cases for the Place class."""

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
        """Test instantiation of Place class."""
        instance = Place()
        self.assertEqual(str(type(instance)), "<class 'models.place.Place'>")
        self.assertIsInstance(instance, Place)
        self.assertTrue(issubclass(type(instance), BaseModel))

    def test_8_attributes(self):
        """Test the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        instance = Place()
        for key, value in attributes.items():
            self.assertTrue(hasattr(instance, key))
            self.assertEqual(type(getattr(instance, key, None)), value)

if __name__ == "__main__":
    unittest.main()

