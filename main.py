# This program is complete 10/27/22

#challenge:
# Create a function in Python that accepts two parameters.
# The first will be a list of numbers.
# The second parameter will be a string that can be one of the following values: asc, desc, and none.

# If the second parameter is "asc," then the function should return a list with the numbers in ascending order.
# If it's "desc," then the list should be in descending order,
# and if it's "none," it should return the original list unaltered.
import string
from string import ascii_letters
import random

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

#put the string and array inputs here:
nums = []
numRange = random.randrange(0,10000)
print(numRange)
for x in range(numRange):
    nums.append(x)

str = ['z','a','z']

# letters = []
# letters.append(string.ascii_letters)
if testStr(str) == 'ascending':
    nums.sort(key = None, reverse=False)
elif testStr(str) == 'descending':
    nums.sort(key = None, reverse=True)

print(nums)