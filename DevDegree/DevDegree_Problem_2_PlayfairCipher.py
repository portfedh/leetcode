# Steps to solve Escape room problem:

'''
1. Found site with explanation of Playfair Cipher.
    https://www.geeksforgeeks.org/playfair-cipher-with-examples/


2. Decrypted message by hand
    - Divide word into pairs
    - Use algorithm to solve
      - If leters are in the same row, use the letter to the left.
      - If letters are in the same column, use the letter on the top. 
      - If letters are in different rows and columns
        - Make a rectangle
        - Use the letter in the oposite corner of the rectangle, same row.

3. Mesagges did not coincide exactly with possible solutions.

4. Looked at code to make the playfair cipher.
    Found a site that offers a working example. 
      https://www.dcode.fr/playfair-cipher

5. Checked my solutions. They coincided. 
    Messages stil did not coincide with possible solutions

6. Went over the possible solutions. 
    Switching the letter order, found the closest answer.
    Selected that answer

''''