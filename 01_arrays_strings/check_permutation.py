"""
Given two strings, decides if one is a permutation of the other.

@author Alejandro Baldominos <me@bal.do>
"""

from collections import Counter

def check_permutation_with_counter (s1 : str, s2 : str) -> bool:
    """
    This proceeds by using a counter, which is a hash
    table mapping characters to number of occurrences. 
    By substracting two counters, and considering that
    the length of the strings are the same, we can
    check whether they contain the same characters.

    We can check whether there are positive elements in
    the counter after the subtraction. If there aren't
    any, then we're done.

    Complexity: O(n)
    """
    if len(s1) != len(s2):
        return False 

    c = Counter(s1)
    c.subtract(s2)
    try:
        next(c.elements())
        return False
    except StopIteration:
        return True


def check_permutation_with_sort (s1 : str, s2 : str) -> bool:
    """
    This proceeds by sorting the two strings and
    comparing whether they are identical. If so,
    then one is a permutation of the other.

    Complexity: O(n * logn)
    """
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    print("Testing strings 'carmina' and 'buranas'");
    print(f"  check_permutation_with_counter: {check_permutation_with_counter('carmina', 'buranas')}");
    print(f"  check_permutation_with_sort: {check_permutation_with_sort('carmina', 'buranas')}");

    print("Testing strings 'moana' and 'manao'");
    print(f"  check_permutation_with_counter: {check_permutation_with_counter('moana', 'manao')}");
    print(f"  check_permutation_with_sort: {check_permutation_with_sort('moana', 'manao')}");