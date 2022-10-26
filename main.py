# Create a function in Python that accepts two parameters.
# The first will be a list of numbers.
# The second parameter will be a string that can be one of the following values: asc, desc, and none.

# If the second parameter is "asc," then the function should return a list with the numbers in ascending order.
# If it's "desc," then the list should be in descending order,
# and if it's "none," it should return the original list unaltered.
import string
from string import ascii_letters
from random import choice

def testStr(str):
    countBuckets = [0,0,0]
    try:
        # if the string is ascending, return asc
        iterchar = iter(str)
        for i in str:
            try:
                if i == str[0]:
                    old = iterchar.__next__()
                    pass
                new = iterchar.__next__()
                print('values are: ', old, ' ', new)
                if new > old:
                    countBuckets[0] = countBuckets[0] + 1
                elif new < old:
                    countBuckets[1] = countBuckets[1] + 1
                else:
                    countBuckets[2] = countBuckets[2] + 1
                old = new
            except:
                break
        #study the results
        if countBuckets[2] != 0:
            return 'none'
        elif (countBuckets[0] != 0) & (countBuckets[1] != 0):
            return 'none'
        elif countBuckets[0] != 0:
            return 'ascending'
        else:
            return 'descending'

    except:
        return "fault"

def sort_list(numList, str):

    return

blop = []
for x in string.ascii_letters():
    ''.join(x)

print(blop)
strasc = blop

print(testStr(strasc))
