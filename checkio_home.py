""" Split List
You have to split a given array into two arrays. If it has an odd amount of elements, 
then the first array should have more elements. If it has no elements, then two empty arrays should be returned.

"""
import math
def split_list(items):
    x = math.ceil(len(items) / 2)
    lg = items[:x]
    ld = items[x:]
    sliced_list = [lg, ld]
    return sliced_list




