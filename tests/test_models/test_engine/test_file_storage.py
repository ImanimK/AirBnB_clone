#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

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

    def test_5_instantiation(self):
        """Test instantiation of storage class."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_3_init_no_args(self):
        """Test __init__ with no arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_3_init_many_args(self):
        """Test __init__ with many arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), msg)

    def test_5_attributes(self):
        """Test class attributes."""
        self.reset_storage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def help_test_all(self, classname):
        """Helper tests all() method for classname."""
        self.reset_storage()
        self.assertEqual(storage.all(), {})

        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)

    def test_5_all_base_model(self):
        """Test all() method for BaseModel."""
        self.help_test_all("BaseModel")

    def test_5_all_user(self):
        """Test all() method for User."""
        self.help_test_all("User")

    def test_5_all_state(self):
        """Test all() method for State."""
        self.help_test_all("State")

    def test_5_all_city(self):
        """Test all() method for City."""
        self.help_test_all("City")

    def test_5_all_amenity(self):
        """Test all() method for Amenity."""
        self.help_test_all("Amenity")

    def test_5_all_place(self):
        """Test all() method for Place."""
        self.help_test_all("Place")

    def test_5_all_review(self):
        """Test all() method for Review."""
        self.help_test_all("Review")

    def help_test_all_multiple(self, classname):
        """Helper tests all() method with many objects for classname."""
        self.reset_storage()
        self.assertEqual(storage.all(), {})

        cls = storage.classes()[classname]
        objs = [cls() for i in range(1000)]
        [storage.new(o) for o in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for o in objs:
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], o)

    def test_5_all_multiple_base_model(self):
        """Test all() method with many objects."""
        self.help_test_all_multiple("BaseModel")

    def test_5_all_multiple_user(self):
        """Test all_multiple() method for User."""
        self.help_test_all_multiple("User")

    def test_5_all_multiple_state(self):
        """Test all_multiple() method for State."""
        self.help_test_all_multiple("State")

    def test_5_all_multiple_city(self):
        """Test all_multiple() method for City."""
        self.help_test_all_multiple("City")

    def test_5_all_multiple_amenity(self):
        """Test all_multiple() method for Amenity."""
        self.help_test_all_multiple("Amenity")

    def test_5_all_multiple_place(self):
        """Test all_multiple() method for Place."""
        self.help_test_all_multiple("Place")

    def test_5_all_multiple_review(self):
        """Test all_multiple() method for Review."""
        self.help_test_all_multiple("Review")

    def test_5_all_no_args(self):
        """Test all() with no arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_all_excess_args(self):
        """Test all() with too many arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 98)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_new(self, classname):
        """Helps tests new() method for classname."""
        self.reset_storage()
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], o)

    def test_5_new_base_model(self):
        """Test new() method for BaseModel."""
        self.help_test_new("BaseModel")

    def test_5_new_user(self):
        """Test

