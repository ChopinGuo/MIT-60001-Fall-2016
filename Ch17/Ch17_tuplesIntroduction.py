# Ch17_tuplesIntroduction.py

# Creating an empty tuple
te = ()
print(te)          # -> ()
print(type(te))    # -> <class 'tuple'>
print(len(te))     # -> 0

# Creating a tuple that contains some elements by seperating each element with
# a comma.
t = (2, "chopin", 3)
print(t)         # evaluates to (2, 'chopin', 3)
# Much like strings, we can indes into tuples to find out values at particular
# indices.
print(t[0])      # evaluates to 2
# Just like strings, we can concatenate tuples together.
print(t + (5,6)) # evaluates to (2, 'chopin', 3, 5, 6)
# Just like strings, We can slice into tuples.
print(t[1:2])    # Slice tuple, evaluates to ('chopin',).
                 # Extra comma means a tuple with one element.
                 # If we did not have this comma here, then this would just be
                 # a string. The parentheses would not really make any
                 # difference.
                 # Remember we go until this stop minus 1.
print(t[1:3])    # Slice tuple, evaluates to ('chopin', 3)
print(len(t))    # evaluates to 3
# And just like strings, if we try to change a value inside a tuple, Python
# does not allow that,
# t[1] = 4         # gives error, can't modify object

# Calculate the quotient and remainder when we divide x by a y.
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

(quot, rem) = quotient_and_remainder(4, 5) # evaluates to (0, 4)
print(quot)                                # evaluates to 0
print(rem)                                 # evaluates to 4
