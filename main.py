'''
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace
the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''


def split_to_pair_of_chars(text):

    text1 = [x for x in text]
    new_text = []
    i = 0
    while i <= len(text1) - 1:
        if i + 1 == len(text1):
            new_text.append(text1[i] + '_')
            break
        new_text.append(text1[i] + text1[i + 1])

        i += 2
    return new_text


split_to_pair_of_chars('abcdefghijk')


'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''


def find_it(seq):

    numbers = [x for x in seq if seq.count(x) % 2]
    i = 0

    while i < len(numbers) and len(numbers) > 1:
        numbers.pop()
        i += 1


def find_it1(seq):

    for x in seq:
        if seq.count(x) % 2:
            return x


def find_it3(seq):
    return [x for x in seq if seq.count(x) % 2][0]


find_it([2, 2, 2, 2, 4, 4, 6, 6, 6])
find_it3([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
find_it1([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
find_it1([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
find_it1([10])
find_it1([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
find_it1([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10])

'''
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical
order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.

Beware: r must be without duplicates.
Don't mutate the inputs.
'''

a1 = ["arp", "live", "strong", "rp"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]


def in_array(a1, a2):
    r = []
    for x in a1:
        for y in a2:
            if x in y and x not in r:
                r.append(x)
    return sorted(r)


def in_array2(a1, a2):
    return sorted([sub for sub in a1 if any(sub in s for s in a2)])




if __name__ == '__main__':
    print('')


