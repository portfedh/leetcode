# DevDegree Problem 6
#####################

# Create alphabet dictionary with number and letter:
####################################################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

range_alpha = len(alphabet)

end_dict = {}

for x in range(len(alphabet)):
    end_dict[alphabet[x]] = x+8

print('Alphabet:\n',end_dict)

# Create functions to test words:
#################################

# Given Words:
##############
# C = 10
# RUBY = 94
# RAILS = 94

def get_word_to_list(word):
    ''' Input a string, returns a list with each string character.'''
    word_list = []
    for x in word:
        word_list.append(x)
    return word_list

def get_number(word_list):
    ''' Input a list with strings, returns a list with each letter number in the alphaber.'''
    number_list = []
    for x in word_list:
        number_list.append(end_dict[x])
    return number_list

def get_sum_number(number_list):
    ''' Input a list with numbers, returns the sum of all the numbers.'''
    subtotal = 0
    for x in number_list:
        subtotal += x
    return subtotal

# Run function
word_list = get_word_to_list('javascript')
print('Word list:\n', word_list)

number_list = get_number(word_list)
print('Number of each word:\n', number_list)

subtotal = get_sum_number(number_list)
print('Subtotal:\n', subtotal)


# Output
########

# Alphabet:
#  {'a': 8, 'b': 9, 'c': 10, 'd': 11, 'e': 12, 'f': 13, 'g': 14, 'h': 15, 'i': 16, 'j': 17, 'k': 18, 'l': 19, 'm': 20, 'n': 21, 'o': 22, 'p': 23, 'q': 24, 'r': 25, 's': 26, 't': 27, 'u': 28, 'v': 29, 'w': 30, 'x': 31, 'y': 32, 'z': 33}
# Word list:
#  ['j', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']
# Number of each word:
#  [17, 8, 29, 8, 26, 10, 25, 16, 23, 27]
# Subtotal:
# 189
