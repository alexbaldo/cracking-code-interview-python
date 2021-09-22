"""
Provides an implementation of a string builder that
allows fast concatenation of strings.

@author Alejandro Baldominos <me@bal.do>
"""

class StringBuilder:

    def __init__ (self, sep : str = ''):
        """
        Creates a new string builder with the specified separator.

        Parameters:
           sep (str): The string separator.
        """
        self.sep = sep
        self.strings = []

    def append (self, s : str):
        """
        Adds a new string at the end of the string builder.

        Parameters:
            s (str): The new string to be appended.
        """
        self.strings.append(s)

    
    def __str__ (self):
        """
        Returns the string representation of all current string builder status.

        Returns:
            string (str): String representation of the current string builder.
        """
        return self.sep.join(self.strings)