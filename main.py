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
















if __name__ == '__main__':
    print('')


