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




def second_index(text, symbol):
    """
    returns the second index of a symbol in a given text
    """
    if symbol == '':
        return None
    if symbol in text:
        return text.rindex(symbol, 2)
    elif symbol not in text:
        return 0 or None



print(second_index('sims', 'a'))

def second_index(text, symbol):
    """
    returns the second index of a symbol in a given text
    """
    
    occurence = 0
    for i in text:
        if i == symbol:
            occurence += 1
            if occurence > 1:
                return text.index(i)



print(second_index('hello', 'l'))




text = 'Hello world'
if 'o' in text:
    print(text.index('o'))