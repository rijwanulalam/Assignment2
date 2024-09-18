# Function to decrypt the text with a given shift key
def decrypt_caesar_cipher(text, shift_key):
    decrypted_text = ""

    for char in text:
        # Decrypt only alphabetic characters (both uppercase and lowercase)
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                decrypted_text += chr(((ord(char) - ord('A') - shift_key) % 26) + ord('A'))
            # Handle lowercase letters
            else:
                decrypted_text += chr(((ord(char) - ord('a') - shift_key) % 26) + ord('a'))
        else:
            # Non-alphabetic characters (such as spaces and punctuation) are not shifted
            decrypted_text += char

    return decrypted_text

# given text
text = '''VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNKX ZVFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQFBAG QRFRER ZR NG ZL ORFG ZNEVYLA ZBAEBR'''

# Try different shift keys to see which gives a meaningful result
for shift_key in range(26):
    decrypted_message = decrypt_caesar_cipher(text, shift_key)
    print(f"Shift key {shift_key}:\n{decrypted_message}\n")

# 13 is the right shift where i got the original quote.