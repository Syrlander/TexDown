"""Formats files, directories and wildcards for incoming string paths"""

import os

def convert_dir_to_files(dir_path):
    """
    Gets a list of all filepaths within a given directory

    Args:
        dir_path: path to directory to get filepaths form

    Returns:
        list of filepath strings,
        None if dir_path not a dir
    """
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            return list(filter(lambda p: os.path.isfile(p), 
                            os.listdir(dir_path)))
    return None


def convert_tilde_wildcard(wildcard_path):
    """
    Converts all wildcards containing the tilde character ('~')

    Args:
        wildcard_path: string path containing the wildcard char

    Returns:
        String containing the converted filepath
    """
    if '~' in wildcard_path:
        user_path = "/home/{0}".format(os.getlogin())
        conv_path = wildcard_path.replace('~', user_path, 1)
        if os.path.exists(conv_path):
            return conv_path
    return None


def convert_star_wildcard(wildcard_path):
    """
    Converts wildcards containg stars ('*')
    
    Args:
        wildcard_path: string path containing the star wildcard

    Returns:
        list of strings containing the filepaths for the specified wildcard_path,
        None if invalid wildcard path
    """
    base = os.path.basename(wildcard_path)
    dir_path = os.path.dirname(wildcard_path)

    # Match for the possible wildcard patterns
    if '*.' in base:
        base_ext = base.split('.')
        base_ext = base_ext[-1]

        return list(filter(lambda p: os.path.isfile(p) and base_ext in p, 
                           os.listdir(dir_path)))
    elif '*' in base:
        return list(filter(lambda p: os.path.isfile(p), 
                           os.listdir(dir_path)))
    return None


def convert_wildcard_path(wildcard_path):
    """
    Converts wildcard formats to lists of filepaths, i.e. 'some_path/*.md' is 
    equal to all files ending in the .md extension within the some_path directory
    or '~/Downloads' will convert the '~' to /home/<SIGN_IN_USER>/
    
    Args:
        wildcard_path: path containing a wildcard

    Returns:
        list of filepath strings
        None, if invalid wildcard_path is given
    """
    return None
