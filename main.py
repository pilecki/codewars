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
print(find_it3([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
find_it1([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
find_it1([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
find_it1([10])
find_it1([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
find_it1([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10])














if __name__ == '__main__':
    print('')


