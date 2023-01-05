"""
Determines if a string has all unique characters.

@author Alejandro Baldominos <me@bal.do>
"""

def is_unique_with_set (s : str) -> bool:
    """
    This proceeds by converting the string to a set and
    comparing the length of the string with the size of
    the set. If both differs, then there are repeated
    elements.

    Complexity: O(n)
    """
    return len(set(s)) == len(s)


def is_unique_with_bitmap (s : str) -> bool:
    """
    This proceeds by using an UTF-8 bitmap to mark
    those existing characters. If a character was
    previously marked, then it is repeated.
    This assumes that the string contains only
    ASCII characters.

    Complexity: O(n)
    """
    bitmap = [0] * 128
    for c in s:
        ix = ord(c)
        if bitmap[ix] == 1:
            return False 
        bitmap[ix] = 1
    return True


def is_unique_with_sort (s : str) -> bool:
    """
    This proceeds by sorting the string and then
    checking whether two consecutive values are
    identical. If that is not the case, then the
    string has unique characters.

    Complexity: O(n * logn)
    """
    chars = sorted(s)
    for i in range(len(chars) - 1):
        if chars[i] == chars[i + 1]:
            return False
    return True


if __name__ == '__main__':
    print("Testing string 'javadoc'");
    print(f"  is_unique_with_set: {is_unique_with_set('javadoc')}");
    print(f"  is_unique_with_bitmap: {is_unique_with_bitmap('javadoc')}");
    print(f"  isUniqueWithSort: {is_unique_with_sort('javadoc')}");

    print("Testing string 'python'");
    print(f"  is_unique_with_set: {is_unique_with_set('python')}");
    print(f"  is_unique_with_bitmap: {is_unique_with_bitmap('python')}");
    print(f"  is_unique_with_sort: {is_unique_with_sort('python')}");