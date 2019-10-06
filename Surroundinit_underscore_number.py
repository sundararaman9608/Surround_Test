import unittest
import subprocess
import os
import shutil

class MyTestCase(unittest.TestCase):

    def test_surround_lowercase_underscore_number(self, name='surroundinit_123'):
        process = subprocess.run(['surround', 'init', '-p', name], encoding='utf-8', stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertIn(process.stdout, "surround: error: Name SURROUNDINIT_123 must be lowercase letters ")

    def test_surround_Uppercase_underscore_number(self, name='SURROUND_123'):
        process = subprocess.run(['surround', 'init', '-p', name], encoding='utf-8', stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertIn(process.stdout, "surround: error: Name SURROUND_123 must be lowercase letters ")

    def test_surround_onlynumber(self, name='123'):
        process = subprocess.run(['surround', 'init', '-p', name], encoding='utf-8', stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertIn(process.stdout, "surround: error: Name 123 must be lowercase letters ")

    def test_surround_underscore_number(self, name='_123'):
        process = subprocess.run(['surround', 'init', '-p', name], encoding='utf-8', stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertIn(process.stdout, "surround: error: Name _123 must be lowercase letters ")






if __name__ == '__main__':
    unittest.main()
