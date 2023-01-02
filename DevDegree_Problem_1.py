keyword_cipher_1 = list('SHOPIFYCOMMERCE')
keyword_cipher_2 = list('TOBILUTKE')

print('Keyword Cypher used:\n', keyword_cipher_1, '\n')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 
            'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

# Create alphabet substitusion
'''
  - Add keyword cipher list to alphabet list
  - Remove duplicates:
      - Create a dictionary from list
      - Make list from dictionary
'''
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
