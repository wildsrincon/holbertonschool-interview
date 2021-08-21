#!/usr/bin/python3
"""
Calculate how much water will be retained after it rains
"""


def rain(walls):
    """
    Calculate water be retained
    """

    retained = 0
    stack = []
    for i in range(len(walls)):
        while stack and walls[i] > walls[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            between = min(walls[i], walls[stack[-1]]) - walls[top]
            retained += distance * between
        stack.append(i)
    return retained
