"""
Replaces all spaces in a string with '%20'.

@author Alejandro Baldominos <me@bal.do>
"""

def urlify_inplace (s : str) -> str:
    """
    We assume that the input string holds enough space as to
    be able the store the URLified string. Since a space originally
    takes 1 character, but takes 3 characters after URLification,
    this means that there are 2*w null characters at the end.

    We will first count the number of spaces by dividing the number of 
    trailing null characters by 2. Then, we will iterate through the
    string backwards moving the complete words two positions to the
    right in order to fill the spaces. As a result, the process is
    performed inplace (although for simplification, the string is
    converted to a list before dealing with it).

    Complexity: O(n)
    """
    a = list(s)

    # Count the number of white spaces.
    num_spaces = 0
    for c in range(len(a)-1, 0, -2):
        if a[c] == '\0':
            num_spaces += 1
        else:
            break
    
    # c (cursor) now points to the last valid symbol in the string.
    # Iterates for the total number of spaces.
    for n in range(num_spaces, 0, -1):
        # Counts the length of the word.
        wordlen = 0
        while a[c] != ' ':   
            wordlen += 1
            c -= 1
        c += 1 # c now points to the first character of the word.

        # Moves the word to the right.
        a[(c + 2 * n):(c + 2 * n + wordlen)] = a[c:(c + wordlen)]

        # Places the '%20' immediately before the moved word.
        a[(c + 2 * n - 3):(c + 2 * n)] = '%20'

        # c is decreased in two units (to "jump" over the space).
        c -= 2
        
    return ''.join(a)


if __name__ == '__main__':
    print("Testing string 'Mr John Smith'")
    print("  urlify_inplace: " + urlify_inplace('Mr John Smith\0\0\0\0'))
