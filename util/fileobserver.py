"""Utility to automatically watch for file changes for a specified file or dir

TODO: Add an Enum class to specify different types of file changes; 
Modified, Created, Deleted and send them as a second argument to 
the callback function.
"""

import os
import repeatedtimer

class FileObserver(object):
    """
    File changes observer
    """

    def __init__(self, paths, callback, interval=5):
        """
        paths: List of file paths to observe
        callback: Callback function to call when a file has been changed.
                  The function will be called with the filename of the changed
                  file, therefore the function passed should take one argument.
        interval: Interval in seconds between each check (default = 5)
        """
        
        self.stamped = [] # list of tuples containing filepaths and timestamps
        self.callback = callback
        self.interval = interval

        self._start_observer(paths)

    def _get_files_to_watch(self, paths):
        """
        Gets initial list of files with timestamps of last modification time
        
        Args:
            paths: list of string filenames to get initial timestamps from
        """
        for path in paths:
            try:
                self.stamped.append((path, os.path.getmtime(path)))
            except FileNotFoundError:
                # If file deleted before getting the initial timestamp (ignore it)
                pass

    def _start_observer(self, paths):
        """
        Starts the repeated execution of the file checking function
        
        Args:
            paths: list of string filenames to make the observer observe
        """
        # Get initial file timestamps
        self._get_files_to_watch(paths)
        
        # Create and start the auto execution of observer function
        repeatedtimer.RepeatedTimer(self.interval, self._check_file_changes)

    def _check_file_changes(self):
        """
        Checks for file changes and executes a callback when a change happens
        """

        def checker(item):
            """
            Checker function used in map, updates timestamp if changes where found
            
            Args:
                item: tuple item containing a filename and timestamp
            
            Returns:
                New tuple item containing filename and timestamp if file changed
            """
            file, stamp = item
            new_stamp = os.path.getmtime(file)
            if os.path.getmtime(file) - stamp > 0:
                self.callback(file)
                stamp = new_stamp
            
            return (file, stamp)

        self.stamped = list(map(checker, self.stamped))
        print(self.stamped)
