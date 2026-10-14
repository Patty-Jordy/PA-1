import monoalph
import caesar
PLAINTEXT_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CIPHERTEXT_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def combo_encipher(message, keyword, shift):
    '''
    Purpose: To encrypt the plaintext message with a monoalph
    keyword and a Caesar shift.

    Parameters: 
        message - the plaintext message to be enciphered; str
        keyword - the keyword used for the monoalph cipher; str 
        shift - the amount to shift each letter; int

    Return Value: The ciphertext that has been encrypted; str
    '''
    encipher_text = ""
    keyword = keyword.upper()
    new_message = ""
    cipher_dict = monoalph.monoalph(keyword)
    for char in message:
        if char in "abcdefghijklmnopqrstuvwxyz":
            secret_letter = cipher_dict[char]
            secret_letter = secret_letter.upper()
            new_message += secret_letter
        else:
            new_message += char
    for char in new_message:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num_position = ord(char) - ord('A')
            shift_char = num_position + shift
            wrap_char = shift_char % 26
            encipher_text += chr(wrap_char + ord('A'))
        else:
            encipher_text += char
    message = encipher_text
    return message
keyword = input("Please input your keyword: ").upper()
message = input("Please input your message: ").lower()
shift = int(input("Please input the number of char you would like to shift by: "))
print(combo_encipher(message, keyword, shift))

def combo_decipher(message, keyword, shift):
    '''
    Purpose: To decrypt the ciphertext message with a monoalph
    keyword and a Caesar shift.

    Parameters:
        message - the ciphertext that needs to be decrypted; str
        keyword - the keyword that was used for the monoalph portion of the encryption; str
        shift - the shift that was used to encrypt the ciphertext; str

    Return Value: The decrypted text; str
    '''
    almost_normal = ""
    cipher_dict = monoalph.monoalph(keyword)
    for char in message:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num_position2 = ord(char) - ord('A')
            shift_char2 = num_position2 - shift
            wrap_char2 = shift_char2 %26
            almost_normal += wrap_char2
        else:
            almost_normal += char
    message2 = ""
    inverse = {}
    for p, c in cipher_dict.items():
        inverse[c] = p
    for char in almost_normal:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uncipher_char = inverse[char]
            message2 += uncipher_char.lower()
        else:
            message2 += char
    message2 = message
    return message
print(combo_decipher(message, keyword, shift))