alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def polyalphabetic(plaintext,codeword):
        ciphertext = ""
        for i in range(len(plaintext)):
                letter = plaintext[i]
                num_in_alphabet = alphabet.index(letter)
 
                # Find the position in the codeword with the letter to shift
                shiftIndex = i % len(codeword)
                
                # Find the letter in the codeword to shift
                shiftLetter = codeword[shiftIndex]
                
                # Find the number associated with the letter to be used as the shift
                shift = alphabet.index(shiftLetter)
                
                cipher_num = (num_in_alphabet + shift) % len(alphabet)
                cipher_letter = alphabet[cipher_num]
                ciphertext = ciphertext + cipher_letter
        return ciphertext
