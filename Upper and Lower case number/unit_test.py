import unittest
import subprocess
import shutil
import os

class MyTestCase(unittest.TestCase):
    def Uppercase_with_Numbers(self):
        process = subprocess.run(['surround', 'init', '-p', 'TEST01'], encoding='utf-8', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertEqual(process.stdout, "surround: error: Name TEST01 must be lowercase letters and underscores only")
    def Lowercase_with_numbets(self):
        process = subprocess.run(['surround', 'init', '-p', 'test01'], encoding='utf-8', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertEqual(process.stdout, "surround: error: Name test01 must be lowercase letters and underscores only")

if __name__ == '__main__':
    unittest.main()
