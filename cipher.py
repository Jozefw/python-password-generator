alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

instructions = input("Type your 'encode' to encode a message, or type 'decode' to decode it:\n").lower()
text = input("Type the message to encode:\n").lower()
shift = int(input("type the shift value:\n"))


def encrypt(test_input, shift_amount):
    cipher_text=""
    for letter in test_input: #hello h
        shifted_position = alphabet.index(letter) + shift_amount #8 3>11
        shifted_position = shifted_position % len(alphabet) #will always give the remainder as the index
        cipher_text += alphabet[shifted_position] # 11 = k
        
    print(f"Here is the encoded result:\n{cipher_text}")    
    
#encrypt(test_input=text, shift_amount=shift)    


def decrypt(decrypt_text, shift_amount):
    de_cipher_text=""
    for letter in decrypt_text: #hello h
        shifted_position = alphabet.index(letter) - shift_amount #8 3>11
        shifted_position = shifted_position % len(alphabet) #will always give the remainder as the index
        de_cipher_text += alphabet[shifted_position] # 11 = k
        
    print(f"Here is the decoded result:\n{de_cipher_text}")    
    
#decrypt(decrypt_text=text,shift_amount=shift)



def cipher(text,shift,trans_code):
    de_cipher_text=""
    for letter in text: #hello h
        if trans_code == "decode":
            shift *=  -1
        shifted_position = alphabet.index(letter) + shift #8 3>11
        shifted_position = shifted_position % len(alphabet) #will always give the remainder as the index
        de_cipher_text += alphabet[shifted_position] # 11 = k
        
    print(f"Here is the decoded result:\n{de_cipher_text}")  
cipher(text,shift,instructions) 