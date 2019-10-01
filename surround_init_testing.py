import unittest
import subprocess


class MyTestCase(unittest.TestCase):
    def test_surround_uppercase(self):
        process = subprocess.run(['surround','init', '-p', 'SURROUNDINIT'], encoding='utf-8', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertIn(process.stdout, "surround: error: Name SURROUNDINIT must be lowercase letters and underscores only ")

    def test_surround_uppercasewithnumber(self):
        process = subprocess.run(['surround','init', '-p', 'SURROUNDINIT123'], encoding='utf-8', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertIn(process.stdout, "surround: error: Name SURROUNDINIT123 must be lowercase letters and underscores only ")

    def test_surround_uppercasewithunderscore(self):
        process = subprocess.run(['surround','init', '-p', 'SURROUNDINIT_123'], encoding='utf-8', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertIn(process.stdout, "surround: error: Name SURROUNDINIT_123 must be lowercase letters and underscores only ")

    def test_surround_uppercasewithsymbol(self):
        process = subprocess.run(['surround','init', '-p', 'SURROUNDINIT*', '-d', 'temp', '-w', 'no'], encoding='utf-8', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertIn(process.stdout, "surround: error: Name SURROUNDINIT* must be lowercase letters and underscores only ")

    def test_surround_lowercase(self):
        process = subprocess.run(['surround','init', '-p', 'surroundinit'], encoding='utf-8', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("captured output is ", process.stdout)
        self.assertIn(process.stdout, "What is the purpose of this project?: ")


if __name__ == '__main__':
    unittest.main()
