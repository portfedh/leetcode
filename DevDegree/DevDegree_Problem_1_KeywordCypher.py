# Secret Keys found in https://devdegree.ca/
keyword_cipher_1 = list('SHOPIFYCOMMERCE')
keyword_cipher_2 = list('TOBILUTKE')

print('Keyword Cypher used:\n', keyword_cipher_1, '\n')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 
            'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

''' Create alphabet substitusion:
  1. Insert keyword cipher list to alphabet list
  2. Remove duplicates:
      a) Create a dictionary from list
      b) Make list from dictionary'''
encrypted_no_duplicates = list(dict.fromkeys(keyword_cipher_1 + alphabet))
print('Alphaber substitution:\n', encrypted_no_duplicates, '\n')

# Create Key
key = {encrypted_no_duplicates[i]: alphabet[i] for i in range(len(encrypted_no_duplicates))}
print('Key:\n', key, '\n')

cipher = list('VIAGUIGTLBILOCSDQN')

message = []
for x in cipher:
    message.append(key[x])

print('Decrypted message is:\n', message)


# Output
########

# Keyword Cypher used:
#  ['S', 'H', 'O', 'P', 'I', 'F', 'Y', 'C', 'O', 'M', 'M', 'E', 'R', 'C', 'E'] 

# Alphaber substitution:
#  ['S', 'H', 'O', 'P', 'I', 'F', 'Y', 'C', 'M', 'E', 'R', 'A', 'B', 'D', 'G', 'J', 'K', 'L', 'N', 'Q', 'T', 'U', 'V', 'W', 'X', 'Z'] 

# Key:
#  {'S': 'A', 'H': 'B', 'O': 'C', 'P': 'D', 'I': 'E', 'F': 'F', 'Y': 'G', 'C': 'H', 'M': 'I', 'E': 'J', 'R': 'K', 'A': 'L', 'B': 'M', 'D': 'N', 'G': 'O', 'J': 'P', 'K': 'Q', 'L': 'R', 'N': 'S', 'Q': 'T', 'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y', 'Z': 'Z'} 

# Decrypted message is:
#  ['W', 'E', 'L', 'O', 'V', 'E', 'O', 'U', 'R', 'M', 'E', 'R', 'C', 'H', 'A', 'N', 'T', 'S']
 