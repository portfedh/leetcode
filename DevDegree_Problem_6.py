# Keys:
#######
# C = 10
# RUBY = 94
# RAILS = 94

# Create Alphabet Key:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

range_alpha = len(alphabet)

end_dict = {}

for x in range(len(alphabet)):
    end_dict[alphabet[x]] = x+8

print('Alphabet:\n',end_dict)


def get_word_to_list(word):
    word_list = []
    for x in word:
        word_list.append(x)
    return word_list


def get_number(word_list):
    number_list = []
    for x in word_list:
        number_list.append(end_dict[x])
    return number_list

def get_sum_number(number_list):
    subtotal = 0
    for x in number_list:
        subtotal += x
    return subtotal


word_list = get_word_to_list('javascript')
print('Word list:\n', word_list)

number_list = get_number(word_list)
print('Number of each word:\n', number_list)

subtotal = get_sum_number(number_list)
print('Subtotal:\n', subtotal)


