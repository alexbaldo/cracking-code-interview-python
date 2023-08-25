"""
Replaces all spaces in a string with '%20'.

@author Alejandro Baldominos <me@bal.do>
"""

def urlify (s : str) -> str:
    """
    This method will create a new array with the required length,
    and then iterate through the string to copy all characters one by one, 
    yet substituting white spaces by '%20'.

    Complexity: O(n)
    """
    # Count the number of white spaces.
    ns = 0
    for c in s:
        if c == ' ':
            ns += 1
    
    # Provisions an empty array with the required length.
    # Since each spaces takes now 3 characters (instead of 1),
    # we need to add 2 * num_spaces to the current string length.
    a = [''] * (len(s) + 2 * ns)

    # We iterate through the string, copying characters
    # one at a time and handling spaces as a special case.
    i = 0
    for c in s:
        if c != ' ':
            a[i] = c
            i += 1
        else:
            a[i:i+3] = '%20'
            i += 3

    return ''.join(a)


if __name__ == '__main__':
    print("Testing string 'Mr John Smith'")
    print("  urlify: " + urlify('Mr John Smith'))
