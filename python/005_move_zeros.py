""" Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0] """

def move_zeros(lst):
    non_zeros = []
    zeros = []

    for num in lst:
        if num != 0:
            non_zeros.append(num)
        else:
                zeros.append(num)
    non_zeros.extend(zeros)
    return (non_zeros)
