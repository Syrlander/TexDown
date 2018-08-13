#/usr/bin/env python3

import unittest
from unittest import mock

from util.pathformatter import *

class TestPathFormatter(unittest.TestCase):
    """Unit testing of the pathformatter util"""

    def setUp(self):
        self.txt_files = ["test_files1.txt", "test_files2.txt", "test_files3.txt"]
        self.py_files = ["test_files4.py", "test_files5.py"]
        self.all_files = self.txt_files + self.py_files

    @mock.patch('util.pathformatter.os.listdir')
    @mock.patch('util.pathformatter.os.path.isfile')
    @mock.patch('util.pathformatter.os.path.isdir')
    @mock.patch('util.pathformatter.os.path.exists')
    def test_convert_dir_to_files(self, mock_os_exists, mock_os_is_dir, mock_os_is_file, mock_os_list_dir):
        """Tests that convert_dir_to_files returns a list of file path strings
        when given a valid directory path"""        
        mock_os_exists.return_value = True
        mock_os_is_dir.return_value = True
        mock_os_is_file.return_value = True
        mock_os_list_dir.return_value = self.all_files
        
        out = convert_dir_to_files("")
        self.assertEqual(out, self.all_files)
    
    @mock.patch('util.pathformatter.os.path.exists')
    def test_convert_dir_nonexisting_path(self, mock_os_exists):
        """Tests that convert_dir_to_files returns None when given a non existing path"""
        mock_os_exists.return_value = False
        out = convert_dir_to_files("")
        self.assertEqual(out, None)

    @mock.patch('util.pathformatter.os.path.exists')
    @mock.patch('util.pathformatter.os.path.isdir')
    def test_convert_dir_none(self, mock_os_is_dir, mock_os_exists):
        """Tests that convert_dir_to_files returns None when given an invalid path"""
        mock_os_is_dir.return_value = False
        mock_os_exists.return_value = True
        out = convert_dir_to_files("")
        self.assertEqual(out, None)

    @mock.patch('util.pathformatter.os.path.exists')
    @mock.patch('util.pathformatter.os.getlogin')
    def test_convert_tilde_wildcard(self, mock_os_getlogin, mock_os_exists):
        """Tests that convert_tilde_wildcard can correctly convert file paths
        containing the tilde character at the beginning of a path string"""
        mock_os_getlogin.return_value = "simon"
        mock_os_exists.return_value = True

        out = convert_tilde_wildcard("~/Downloads/")
        self.assertEqual(out, "/home/simon/Downloads/")

    @mock.patch('util.pathformatter.os.path.exists')
    def test_convert_tilde_wildcard_invalid_path(self, mock_os_exists):
        """Tests that convert_tilde_wildcard returns None when given a wildcard
        path containing an invalidly positioned tilde character"""
        mock_os_exists.return_value = False

        out = convert_tilde_wildcard("somewhere/~/")
        self.assertEqual(out, None)

    def test_convert_tilde_wildcard_no_tilde(self):
        """Tests that convert_tilde_wildcard returns None when given a path not
        containing a tilde character"""
        out = convert_tilde_wildcard("")
        self.assertEqual(out, None)

    @mock.patch('util.pathformatter.os.listdir')
    @mock.patch('util.pathformatter.os.path.isfile')
    def test_convert_star_dot_wildcard(self, mock_os_is_file, mock_os_listdir):
        """Tests that convert_star_wildcard returns a list of string file paths
        when given a wildcard path containing a '*.' sequence"""
        mock_os_is_file.return_value = True
        mock_os_listdir.return_value = self.txt_files

        out = convert_star_wildcard("./test_files/*.txt")
        self.assertEqual(out, self.txt_files)

    @mock.patch('util.pathformatter.os.listdir')
    @mock.patch('util.pathformatter.os.path.isfile')
    def test_convert_star_wildcard(self, mock_os_is_file, mock_os_listdir):
        """Test that convert_star_wildcard returns a list of string file paths
        when given a wildcard path containing a '*' char"""
        mock_os_is_file.return_value = True
        mock_os_listdir.return_value = self.all_files

        out = convert_star_wildcard("./test_files/*")
        self.assertEqual(out, self.all_files)

    @mock.patch('util.pathformatter.os.listdir')
    @mock.patch('util.pathformatter.os.path.isfile')
    def test_convert_stardot_path(self, mock_os_is_file, mock_os_listdir):
        """Tests that convert_wildcard_path can convert a path containing the
        star dot wildcard; '*.'"""
        mock_os_is_file.return_value = True
        mock_os_listdir.return_value = self.txt_files

        out = convert_wildcard_path("./test_files/*.txt")
        self.assertEqual(out, self.txt_files)

    @mock.patch('util.pathformatter.os.listdir')
    @mock.patch('util.pathformatter.os.path.isfile')
    def test_convert_star_path(self, mock_os_is_file, mock_os_listdir):
        """Tests that convert_wildcard_path can convert a path containing the
        star wildcard; '*'"""
        mock_os_is_file.return_value = True
        mock_os_listdir.return_value = self.all_files

        out = convert_wildcard_path("./test_files/*")
        self.assertEqual(out, self.all_files)

    @mock.patch('util.pathformatter.os.getlogin')
    @mock.patch('util.pathformatter.os.path.exists')
    def test_convert_tilde_path(self, mock_os_exists, mock_os_getlogin):
        """Tests that convert_wildcard_path can convert a path containing the
        tilde wildcard; '~'"""
        mock_os_exists.return_value = True
        mock_os_getlogin.return_value = 'simon'

        out = convert_wildcard_path("~/Downloads/")
        self.assertEqual(out, "/home/simon/Downloads/")

    def test_convert_multiple_wildcards(self):
        """Tests that convert_wildcard_path can convert a path containing
        multiple wildcards"""
        
        out = convert_wildcard_path("")
        self.assertEqual(out, [])

if __name__ == '__main__':
    unittest.main()
