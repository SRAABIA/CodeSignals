'''
Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag. More formally, your task is to construct an array of length numbers.length - 2, where the ith element of the output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

Example

For numbers = [1, 2, 1, 3, 4], the output should be solution(numbers) = [1, 1, 0].

(numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;
(numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;
(numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;

'''

def solution(numbers):
    outputarr = []
    x = len(numbers)-2
    for i in range(len(numbers)):
        if i+1 < len(numbers) and i+2 < len(numbers):
            if (numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2]) or (numbers[i] > numbers[i+1] and numbers[i+1] < numbers[i+2]):
                outputarr.append(1)
            else:
                outputarr.append(0)
    return outputarr
