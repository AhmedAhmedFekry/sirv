import math


def solution(inputString):
    list1=list(inputString)
    print(list1)
    list2=list1.reverse()
    # list2=list(reversed(inputString))
    print(list2)
    print(list1==list2)
solution("aabaa")