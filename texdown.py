#!/usr/bin/env python3
""""Program to simply convert Markdown files with embedded TeX math to pdf's"""

import os
import argparse

from util import fileobserver
from util import pathformatter
from util import config

# # Supported markdown file extensions
# valid_file_extensions = [
#     'markdown',
#     'mdown',
#     'mkdn',
#     'md',
#     'mkd',
#     'mdwn',
#     'mdtxt',
#     'mdtext',
#     'text',
#     'Rmd'
# ]


# def validate_file_extensions(files):
#     """Validates that every file is a markdown file
    
#     Throws: ValueError, file with invalid file extension"""
#     for file in files:
#         if file.name.split('.')[-1] not in valid_file_extensions:
#             raise ValueError('Error: Found file with invalid file extensions: \
#                              {0}'.format(file.name))


# def validate_folder_existance(folder):
#     """Validates that a given directory exists

#     Throws: ValueError, folder doesn't exist"""
#     if folder:
#         if not os.path.exists(folder) or not os.path.isdir(folder):
#             raise ValueError('Error: Invalid output folder given: \
#                              {0}'.format(folder))


# def try_convert_files(files, out_folder=os.getcwd()):
#     """Tries to convert the given files to pdf's, and output them in the 
#     specified output folder"""
#     if files:
#         # Validation
#         validate_file_extensions(files)
#         validate_folder_existance(out_folder)

#         # Format the valid output folder
#         if out_folder[-1] is not '/':
#             out_folder += '/'

#         # Convert the files
#         for file in files:
#             filename = file.name.split('.')[0]
            
#             os.system('pandoc {0} -o {1}{2}.pdf'.format(
#                 file.name, out_folder, filename))

def validate_file(filepath):
    """
    Validates that a single file exsists and is of a valid file extension

    Args:
        filepath: path of file to validate

    Returns:
        True: File is valid
        Flase: File is invalid
    """
    retVal = False
    
    if os.path.exists(filepath):
        if os.path.isfile(filepath):
            base = os.path.basename(filepath)
            base_ext = base.split('.')[-1]
            
            if base_ext in config.VALID_FILE_EXTENSIONS:
                retVal = True

    return retVal

def try_convert_pandoc(filepath, output="./output/"):
    """
    Converts a validated markdown file to pdf format using Pandoc

    Args:
        filepath: path of file to convert
        output: output folder for pandoc to convert files into (default: './output/')

    Returns:
        True: Conversion was successful
        False: Conversion failed or another error occured
    """
    pass

def execute_converter(pargs):
    """
    Handles the execution of the conversions

    Args:
        pargs: parser arguments; the values gotten from the argparse parser
    """
    pass

def main():
    # Create argparser setup
    parser = argparse.ArgumentParser(prog="TexDown", description=
        "Converts Markdown files with embedded Tex math to pdf")

    parser.add_argument('to_convert', nargs='+', 
                        help='Markdown files to convert')
    parser.add_argument('-o', '--output', 
                        help='Folder to place pdf\'s in')
    parser.add_argument('-a', '--auto', action='store_true', 
                        help='Enable auto conversion flag')

    # Parse and convert
    execute_converter(parser.parse_args())

if __name__ == '__main__':
    main()
