#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import json
import os
import re
import time
import unittest
from datetime import datetime
import uuid

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):

    """Test Cases for the BaseModel class."""

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

    def test_3_instantiation(self):
        """Test instantiation of BaseModel class."""
        instance = BaseModel()
        self.assertEqual(str(type(instance)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(issubclass(type(instance), BaseModel))

    def test_3_init_no_args(self):
        """Test __init__ with no arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    # Grouping related tests
    def test_3_attributes(self):
        """Test attributes value for an instance of a BaseModel class."""
        attributes = storage.attributes()["BaseModel"]
        instance = BaseModel()
        for key, value in attributes.items():
            self.assertTrue(hasattr(instance, key))
            self.assertEqual(type(getattr(instance, key, None)), value)

    def test_3_datetime_created(self):
        """Test if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        instance = BaseModel()
        diff = instance.updated_at - instance.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = instance.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_3_id(self):
        """Test for unique user ids."""
        id_list = [BaseModel().id for _ in range(1000)]
        self.assertEqual(len(set(id_list)), len(id_list))

    # Grouping related tests
    def test_3_save(self):
        """Test the public instance method save()."""
        instance = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        instance.save()
        diff = instance.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    # Grouping related tests
    def test_3_str(self):
        """Test for __str__ method."""
        instance = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(instance))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), instance.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = instance.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    # Grouping related tests
    def test_3_to_dict(self):
        """Test the public instance method to_dict()."""
        instance = BaseModel()
        instance.name = "Laura"
        instance.age = 23
        d = instance.to_dict()
        self.assertEqual(d["id"], instance.id)
        self.assertEqual(d["__class__"], type(instance).__name__)
        self.assertEqual(d["created_at"], instance.created_at.isoformat())
        self.assertEqual(d["updated_at"], instance.updated_at.isoformat())
        self.assertEqual(d["name"], instance.name)
        self.assertEqual(d["age"], instance.age)

    def test_3_to_dict_no_args(self):
        """Test to_dict() with no arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_to_dict_excess_args(self):
        """Test to_dict() with too many arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    # Grouping related tests
    def test_4_instantiation(self):
        """Test instantiation with **kwargs."""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    # Grouping related tests
    def test_4_instantiation_dict(self):
        """Test instantiation with **kwargs from custom dict."""
        custom_dict = {
            "__class__": "BaseModel",
            "updated_at": datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
            "created_at": datetime.now().isoformat(),
            "id": uuid.uuid4(),
            "var": "foobar",
            "int": 108,
            "float": 3.14
        }
        instance = BaseModel(**custom_dict)
        self.assertEqual(instance.to_dict(), custom_dict)

    # Grouping related tests
    def test_5_save(self):
        """Test that storage.save() is called from save()."""
        self.reset_storage()
        instance = BaseModel()
        instance.save()
        key = "{}.{}".format(type(instance).__name__, instance.id)
        data = {key: instance.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(data)))
            f.seek(0)
            self.assertEqual(json.load(f), data)

    def test_5_save_no_args(self):
        """Test save() with no arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """Test save() with too many arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

if __name__ == '__main__':
    unittest.main()

