import unittest

import app.phonebook as phonebook

class test_phonebook(unittest.TestCase):
    
    def test_add_contact(self):
        response = phonebook.add_contact("Kezzy", "0788888888")
        self.assertEqual(response["message"], "Contact Added successfully")

    def test_update_contact(self):
        response = phonebook.update_contact({"Kezzy", "0788888888" },{"Ann", "0799988888"})
        self.assertEqual(response["message"], "Contact updated successfully")

    def test_delete_contact(self):
        response = phonebook.delete_contact("Kezzy", "0788888888")
        self.assertEqual(response["message"], "Contact deleted")

    def test_view_contact(self):
        response = phonebook.view_contact("Kezzy", "0788888888")
        self.assertEqual(response["message"], "Contact found")