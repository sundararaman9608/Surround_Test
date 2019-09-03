import unittest
import subprocess
import shutil


class MyTestCase(unittest.TestCase):

#validating the surround init command line functionality
#verfiying the output after the surround init command
    def test_surround_init(self):
        process1= subprocess.run(["surround", "init"], encoding='utf-8', stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        print("Output captured:", process1.stdout)
        self.assertEqual(process1.stdout, "Name of project: ")

#

    def test_surround_init_lowercase(self):
        process = subprocess.run(["surround", "init",'-p','tempo','-d','temporary','-w','no'], encoding='utf-8',
                                 stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        print("Output captured:", process.stdout)
        self.assertIn(process.stdout, "info: project created at C:\\Users\\sunda\\Surround_Test\\tempo\n")
        shutil.rmtree('tempo')

    def test_surround_init_lowercase_underscore(self):
        process = subprocess.run(["surround", "init", '-p', 'tempo', '-d', 'temporary', '-w', 'no'], encoding='utf-8',
                                 stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Output captured:", process.stdout)
        self.assertIn(process.stdout, "info: project created at C:\\Users\\sunda\\Surround_Test\\tempo\n")
        shutil.rmtree('tempo')

    def test_surround_init_lowercase_symbol(self):
        process = subprocess.run(["surround", "init", '-p','user#','-d','temporary','w','no'], encoding='utf-8',
                                 stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Output captured:", process.stdout)
        self.assertIn(process.stdout, " surround: error: Name user# must be lowercase letters ")

    def test_surround_init_only_symbol(self):
        process = subprocess.run(["surround", "init", '-p', ',#*@$', '-d', 'temporary', 'w', 'no'], encoding='utf-8',
                                 stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Output captured:", process.stdout)
        self.assertIn(process.stdout, " surround: error: Name #*@$' must be lowercase letters ")

    def test_surround_init_lowercase_number(self):
        process = subprocess.run(["surround", "init", '-p','user123','-d','temporary','w','no'], encoding='utf-8',
                                 stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Output captured:", process.stdout)
        self.assertIn(process.stdout, " surround: error: Name user123 must be lowercase letters ")
    def test_surround_lint(self):
        process=subprocess.run(["surround", "lint"], encoding='utf-8',
                   stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Output captured:", process.stdout)
        self.assertIn(process.stdout, " TypeError: 'validator' should be of class Validator ")
if __name__ == '__main__':
    unittest.main()
