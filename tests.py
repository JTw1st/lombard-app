import os
import unittest

from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR

import utils as app


class TestMyApp(unittest.TestCase):
    def test_write_file(self):
        os.chmod(app.FILENAME, S_IREAD|S_IRGRP|S_IROTH)
        with self.assertRaises(PermissionError):
            app.save_data({})
        os.chmod(app.FILENAME, S_IWUSR|S_IREAD)

    def test_add_data(self):
        data = {"1": {"Title": "TV", "Price": "105$"}}
        new_data = ["Ring", "10$"]
        self.assertEqual(
            app.add_data(new_data, data),
            {
                "1": {"Title": "TV", "Price": "105$"},
                "2": {"Title": "Ring", "Price": "10$"}
            }
        )
        data = ""
        with self.assertRaises(AttributeError):
            app.add_data(new_data, data)

    def test_delete_data(self):
        data = {
            "1": {"Title": "TV", "Price": "105$"},
            "2": {"Title": "Ring", "Price": "10$"}
        }
        delete_value = "Ring"
        self.assertTrue(
            app.delete_data(data, delete_value)
        )
        delete_value = "Rings"
        self.assertFalse(
            app.delete_data(data, delete_value)
        )

    def test_search_data(self):
        data = {
            "1": {"Title": "TV", "Price": "105$"},
            "2": {"Title": "Ring", "Price": "10$"}
        }
        search_value = "Ring"
        self.assertEqual(
            app.search_data(data, search_value),
            "2|Ring|10$"
        )
        search_value = "Rings"
        self.assertIsNone(
            app.search_data(data, search_value)
        )

    def test_display_data(self):
        data = {
            "1": {"Title": "TV", "Price": "105$"},
            "2": {"Title": "Ring", "Price": "10$"}
        }
        self.assertEqual(
            app.display_data(data),
            "ID|Title|Price\n1|TV|105$\n2|Ring|10$"
        )
        data = {}
        self.assertEqual(
            app.display_data(data),
            "No data"
        )
