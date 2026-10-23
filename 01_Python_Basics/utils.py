"""
Helper functions: a small custom module.

It is imported by 04_core_concepts.py to demonstrate importing your own module.
Keep both files in the same folder so the import works.
"""

#========================
# REMOVE CONSECUTIVE DUPLICATE LETTERS
#========================
def delete_letter(word):
    """Remove consecutive repeated letters using recursion.

    Example: delete_letter("aaabbc") --> "abc"
    """
    if len(word) == 1:  # base case: nothing left to compare
        return word

    if word[0] == word[1]:
        return delete_letter(word[1:])  # skip the repeated first letter

    return word[0] + delete_letter(word[1:])


#========================
# FACTORIAL
#========================
def factorial(n):
    """Return n! using recursion.

    Example: factorial(5) --> 120
    """
    if n in (0, 1):  # base case
        return 1

    return n * factorial(n - 1)