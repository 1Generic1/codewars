"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
"""

def solution(number):
    n = number
    if (n < 0):
        return (0)
    
    #we initialize sum to keep track of the sum of the multiples
    sum = 0
    for i in range(n):
    #if i when divided by 3 or 5 has no remainded that means i is a multiple of 3 or 5 then add i to the sum
        if i % 3 == 0 or i % 5 == 0:
         sum += i
        
    return (sum)
