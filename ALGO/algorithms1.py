"""
First recurring character

Given a string, return the first recurring letter that appears. If there are no recurring letters, return None.

Example:
Input: qwertty
Output:t
"""

def first_recurring_character(s):
    seen_so_far=set()

    for c in s:
        if c in seen_so_far:
            return c
        seen_so_far.add(c)
    
    return None

print(first_recurring_character('qqwertty'))

print(first_recurring_character('qwerty'))
