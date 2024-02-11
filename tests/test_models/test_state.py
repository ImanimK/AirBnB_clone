#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestState(unittest.TestCase):

    """Test Cases for the State class."""

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
        """Test instantiation of State class."""
        instance = State()
        self.assertEqual(str(type(instance)), "<class 'models.state.State'>")
        self.assertIsInstance(instance, State)
        self.assertTrue(issubclass(type(instance), BaseModel))

    def test_8_attributes(self):
        """Test the attributes of State class."""
        attributes = storage.attributes()["State"]
        instance = State()
        for key, value in attributes.items():
            self.assertTrue(hasattr(instance, key))
            self.assertEqual(type(getattr(instance, key, None)), value)

if __name__ == "__main__":
    unittest.main()

