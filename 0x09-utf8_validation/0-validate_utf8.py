#!/usr/bin/python3
'''
Write a method that determines if a given data set represents
a valid UTF-8 encoding
'''


def validUTF8(data):
    '''
    validUTF8 - Determine if a data set represents a valid UTF-8 encoding
    @data: The data set to evaluate
    Return: True if valid UTF-8, False otherwise
    '''
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for number in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & number:
                num_bytes += 1
                mask = mask >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (number & mask1 and not (number & mask2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
