```python
def encipher(message, key)
```
1. encipher_text defined as empty string; ""
1. message set to uppercase; message.upper()
1. for loop for char in message; for char in message:

    a. if char is in uppercase alphabet; if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    
        I. num_position defined the unicode character - unicode 'A'; ord(char) - ord('A')

        II. shift_char defined as num_position + key; num_position + key 

        III. wrap_char defined as shift_char modulo 26; shift_char % 26

        IV. encipher_text defined as the turning the unicode integer of (wrap_char + ord) into a character; += chr(wrap_char + ord("A"))
    
    b. else, char is added to encipher_text; += char

1. return strings key, message

```python
def decipher(message, key)
```
1. normal text defined as empty string; ""
1. for loop for char in message; for char in message: 

    a. if char is in uppercase alphabet; if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        I. num_position2 defined as unicode character - unicode 'A'; ord(char) - ord('A')

        II. shift_char2 defined as num_position2 - key; num_position2 - key

        III. wrap_char2 defined as shift_char2 modulo 26; shift_char2 % 26

        IV. wrap_char2 added to normal_text; += wrap_char2
    
    b. else, char is added to normal text; += char
1. message defined as lowercase normal_text; normal_text.lower()
1. return strings key, message