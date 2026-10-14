from monoalph import PLAINTEXT_ALPHABET
from monoalph import CIPHERTEXT_ALPHABET


def encipher(message, key):
    """
    Encrypt a message using the Caesar cipher.

    Purpose:
        Shift each letter forward by key positions in the alphabet.
        Ciphertext should be in uppercase and leave nonalphabetic characters and 
        punctuation unchanged.

    Parameters:
        message: The plaintext message to encrypt; str
        key: The number of positions to shift each letter.
            Negative values shift letters backward; int

    Return Value:
        The encrypted message; int

    Examples:
        >>> encipher("abc xyz", 3)
        'DEF ABC'
        >>> encipher("xyz", 3)
        'ABC'
        >>> encipher("hello, world!", 3)
        'KHOOR, ZRUOG!'
        >>> encipher("abc", 0)
        'ABC'
        >>> encipher("abc", 3)
        'DEF'
        >>> encipher("", 3)
        ''
    """
    encipher_text = ""
    message = message.upper()
    for char in message:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num_position = ord(char) - ord('A')
            shift_char = num_position + key 
            wrap_char = shift_char % 26
            encipher_text += chr(wrap_char + ord("A"))
        else:
            encipher_text += char
    message = encipher_text
    return key, message
message = input("Input your message: ").lower()
key = int(input("Input a number to shift the letters by: "))
print(encipher(message, key))



def decipher(message, key):
    """
    Decrypt a message encrypted using the Caesar cipher.

    Purpose:
        Shift each letter backward by key positions in the alphabet.
        Plaintext should be in uppercase and leave nonalphabetic characters 
        and punctuation unchanged.

    Parameters:
        message: The ciphertext message to decrypt; str
        key: The shift value used during encryption; int

    Return Value:
        The decrypted plaintext message; str

    Examples:
        >>> decipher("DEF ABC", 3)
        'abc xyz'
        >>> decipher("KHOOR, ZRUOG!", 3)
        'hello, world!'
        >>> decipher("DEF", 29)
        'abc'
        >>> decipher("ZAB", -1)
        'abc'
        >>> decipher("", 3)
        ''
    """
    normal_text = ""
    for char in message: 
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num_position2 = ord(char) - ord('A')
            shift_char2 = num_position2 - key
            wrap_char2 = shift_char2 % 26
            normal_text += wrap_char2
        else:
            normal_text += char
    message = normal_text.lower()
    return key, message
print(decipher(message, key))




