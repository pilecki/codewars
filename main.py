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


def queue_time(customers, n):
    if not customers:
        return 0
    tills = customers[:n]

    customers = customers[n:]

    customers.reverse()

    i = 1
    while customers:
        tills.sort()

        tills[0] += customers.pop()

        i += 1
    return max(tills)

# print(queue_time([2, 2, 3, 5, 6, 8, 1, 1], 50))
# print(50 * '-')
# print(queue_time([2, 3, 4, 20, 7, 8], 20))



def oblicz(a, n):

    kasy = a[:n]
    klient = a[n:]
    kasy.sort()

    for x in range(len(klient)):
        kasy.sort()
        kasy[0] += klient[x]
    r = max(kasy)
    return r

# print(oblicz([2, 3, 4, 20, 7, 8], 30))
# print(oblicz([2, 2, 3, 5, 6, 8, 1, 1], 50))

'''
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''

def create_phone_number(n):
#liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    liczby1 = ''
    for x in n:
        if liczby1 == '':
            liczby1 += '('
        elif len(liczby1) == 4:
            liczby1 += ') '
        elif len(liczby1) == 9:
            liczby1 += '-'
        liczby1 += str(x)
    return liczby1

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


def create_phone_number1(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def silnia(n):
    print(n)
    if n == 0:
        return 1
    return n * silnia(n-1)

print(silnia(3))

'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a 
hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. 
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''


def hexy(a, b, c):

    if a > 255:
        a = 255
    if a < 0:
        a = 0
    if b > 255:
        b = 255
    if b < 0:
        b = 0
    if c > 255:
        c = 255
    if c < 0:
        c = 0

    num = [a, b, c]

    num_array = [hex(x) for x in num]

    num_array1 = ''.join([x[2:] if len(x) == 4 else x[1:] for x in num_array])
    num_array2 = num_array1.replace('x', '0').upper()

    return num_array2


print(hexy(-20, 275, 125))



''' Checking isograms'''

def spr1(n):

    c = n.lower()

    return False if False in [True if c.count(x) == 1 else False for x in c] else True


print(spr1('Dermatoglyphics'))


def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True


if __name__ == '__main__':
    print('')


