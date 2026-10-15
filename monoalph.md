```python
def monoalph(keyword)
```
1. keyword defined as uppercase keyword; keyword.upper()
1. cipher_key defined as empty string; ""
1. for loop for letter in (keyword plus ciphertext_alphabet); for letter in keyword + CIPHERTEXT_ALPHABET:

    a. if letter is in ciphertext_alphabet and letter isn't in cipher_key; if letter in CIPHERTEXT_ALPHABET and letter not in cipher_key:

        I. letter added to cipher_key; += letter
1. return the combined and upacked dictionaries: plaintext_alphabet, cipher_key

```python
def decipher_dict(cipher_dict)
```
1. cipher_dict defined as monoalph(keyword) function; monoalph(keyword)
1. new_cipher defined as empty dictionary; new_cipher = {}
1. for loop for p (plaintext_alphabet) and c (ciphertext_alphabet) in returned value pairs in dictionary (tuples); for p, c in cipher_dict.items():

    a. new_cipher stores c as key and p as value; new_cipher[c] = p
1. return dictionary new_cipher
1. cipher_dict defined as function monoalph(keyword)

```python
def encipher(message, cipher_dict)
```
1. new_message defined as empty string; ""
1. message set as lowercase message; message.lower()
1. for loop for char in message; for char in message:

    a. if char is in lowercase alphabet; if char in "abcdefghijklmnopqrstuvwxyz":

        I. secret_letter defined as char mapped into cipher_dict; cipher_dict[char]

        II. secret_letter defined as uppercase secret_letter; secret_letter.upper()

        III. secret_letter added to new_message; += secret_letter
    
    b. else, char added to new_message; += char
1. return new_message

```python
def decipher(message, cipher_dict)
```
1. message2 defined as empty string; ""
1. inverse defined as empty dictionary; {}
1. for loop for p (plaintext_alphabet), c (ciphertext_alphabet) in returned value pairs in cipher_dict dictionary; for p, c in cipher_dict.items():

    a. inverse dictionary stores p, and c as its matching cipher; inverse[c] = p
1. for loop for char in message; for char in message:
    
    a. if char in uppercase alphabet; if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        I. uncipher_char defined as char inputed into inverse dictionary; inverse[char]

        II. lowercase uncipher_char added to message2; += uncipher_char.lower()
    
    b. else, char added to message2; += char

1. return message2
