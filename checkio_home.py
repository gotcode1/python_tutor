""" Split List
You have to split a given array into two arrays. If it has an odd amount of elements, 
then the first array should have more elements. If it has no elements, then two empty arrays should be returned.

"""
import math
import re
import string
def split_list(items):
    x = math.ceil(len(items) / 2)
    lg = items[:x]
    ld = items[x:]
    sliced_list = [lg, ld]
    return sliced_list

""" Return true if all elements in the list are the same or if list is empty or if list contain 1 element, else return false"""
def all_the_same(elements):
    ouff = set(elements)
    if len(elements) == 0:
        return True
    if len(ouff) == 1:
        return True
    return False

def second_index(text, symbol):
    """
    returns the second index of a symbol in a given text
    """
    first_occ = text.find(symbol)
    second_occ = text.find(symbol, first_occ + 1)
    if symbol not in text:
        return None
    elif second_occ < 2:
        return None
    else:
        return text.find(symbol, first_occ + 1)





def popular_words(text, words):
    list_of_words = text.translate(str.maketrans('', '', string.punctuation))
    l3 = list(list_of_words.split())
    my_dict = {}
    oc_times = []
    for i in l3:
        if i in words:
            counter_occurence = list_of_words.count(i)
            # oc_times.append(counter_occurence)
            # my_dict = dict(zip(words, oc_times))
            my_dict.update({i : counter_occurence})
    
    return my_dict

print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))





"""Return sorted list elements in the decreasing frequency order (i.e. the number of times they appear in elements."""
def frequency_sort(items):
    # your code here
    return None


