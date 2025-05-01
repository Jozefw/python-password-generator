alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#instructions = input("Type your 'encode' to encode a message, or type 'decode' to decode it:\n").lower()
text = input("Type the message to encode:\n").lower()
shift = int(input("type the shift value:\n"))


def encrypt(test_input, shift_amount):
    cipher_text=""
    for letter in test_input: #hello h
        shifted_position = alphabet.index(letter) + shift_amount #8 3>11
        cipher_text += alphabet[shifted_position] # 11 = k
        
    print(f"Here is the encoded result:{cipher_text}")    
    
encrypt(test_input=text, shift_amount=shift)    