```python
def combo_encipher(message, keyword, shift)
```
1. encipher_text defined as empty string; ""
1. keyword set to uppercase keyword; keyword.upper()
1. new_message defined as empty string; ""
1. cipher_dict defined as imported monoalph.monoalph(keyword) function; monoalph.monoalph(keyword)
1. for loop for character in message; for char in message:
    
    a. if character is in lowercase alphabet; if char in "abcdefghijklmnopqrstuvwxyz":

        I. secret_letter defined as char inputed into cipher_dict dictionary; cipher_dict[char]

        II. secret_letter set to uppercase; secret_letter.upper()

        III. secret letter added to new_message; += secret_letter
    
    b. else, char added to new message; += char
1. for loop for character in new_message; for char in new_message:

    a. if char in uppercase alphabet; if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        I. num_position defined as unicode character - unicode 'A'; ord(char) - ord('A')
        II. shift_char defined as num_position + shift; num_position + shift

        III. wrap_char defined as shift_char modulo 26; shift_char % 26

        IV. Corresponding char to wrap_char + unicode 'A' added to encipher_text; += chr(wrap_char + ord('A'))

    b. else, character added to encipher_text; += char
1. message defined as encipher_text
1. return string message

```python
def combo_decipher(message, keyword, shift)
```
1. almost_normal defined as empty string; ""
1. cipher_dict defined as imported monoalph.monoalph(keyword) function; monoalph.monoalph(keyword)
1. for character in message; for char in message:

    a. if character in uppercase alphabet; if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        I. num_position2 defined as unicode character - unicode 'A'; ord(char) - ord('A')

        II. shift_char2 defined as num_position2 - shift; num_position2 - shift

        III. wrap_char2 defined as shift_char2 modulo 26; shift_char2 %26

        IV. wrapchar2 added to almost_normal; += wrap_char2

    b. character added to almost_normal; += char
1. message2 defined as empty string; ""
1. inverse defined as empty dictionary; {}
1. for loop for p (plaintext_alphabet), c (cipher_text alphabet) in returned value pairs in cipher_text dictionary; for p, c in cipher_dict.items():

    a. inverse dictionary stores p, and c as its matching cipher; inverse[c] = p
1. for loop for character in almost_normal; for char in almost_normal:

    a. if character is in uppercase alphabet; if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        I. uncipher_char defined as character inputed into inverse dictionary; inverse[char]
    
        II. lowercase uncipher_char added to message2; += uncipher_char.lower()

    b. else, character added to message2; += char
1. message defined as message2; message
1. return message
