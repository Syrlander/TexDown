#!/usr/bin/env python3
""""Program to simply convert Markdown files with embedded TeX math to pdf's"""

import os
import sys
import argparse

from util import fileobserver
from util import config


def die(msg):
    """
    Prints an exit message, then kills the application

    Args:
        msg: exit message to print
    """
    print(msg)
    sys.exit()


def validate_file(filepath):
    """
    Validates that a single file exists and is of a valid file extension

    Args:
        filepath: path of file to validate

    Returns:
        True: File is valid
        Flase: File is invalid
    """    
    if os.path.exists(filepath):
        if os.path.isfile(filepath):
            base = os.path.basename(filepath)
            base_ext = base.split('.')[-1]
            
            if base_ext in config.VALID_FILE_EXTENSIONS:
                return True

    return False


def try_convert_pandoc(filepath, output="./pdf_output/"):
    """
    Tries to convert a validated markdown file to pdf using Pandoc

    Args:
        filepath: path of file to convert
        output: output folder for pandoc to convert files into (default: './pdf_output/')

    Returns:
        True: Conversion was successful
        False: Conversion failed or another error occured
    """
    filename = os.path.basename(filepath).split('.')[0]

    resp_code = os.system('pandoc {0} -o {1}{2}.pdf'.format(
        filepath, output, filename))

    if resp_code == 0:
        return True
    return False


def execute_converter(pargs):
    """
    Handles the execution of the conversions

    Args:
        pargs: parser arguments; the values gotten from the argparse parser
    """
    out_folder = "./pdf_output/"
    if pargs.output:
        out_folder = pargs.output

    if not os.path.exists(out_folder):
        os.mkdir(out_folder)

    def helper_func(file):
        """Executes the actual conersion of a single file
        
        Args:
            file: file to convert
        """
        if validate_file(file):
            if not try_convert_pandoc(file, out_folder):
                die("Error: Unable to convert file: {0}".format(file))
            else:
                print("Successfully converted file: {0}".format(file))
        else:
            die("Error: Invalid filepath: {0}".format(file))

    if pargs.auto:
        # Auto check for file changes, then convert
        try:
            fileobserver.FileObserver(pargs.to_convert, helper_func)
        except KeyboardInterrupt:
            die("")
    else:
        # Run once
        for file in pargs.to_convert:
            helper_func(file)

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
