alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
def caesar(plaintext,shift):  
    ciphertext = ""
    for i in range(len(plaintext)):         
        letter = plaintext[i] 
        # find the number position of the ith letter
        num_in_alphabet = alphabet.index(letter) 
        # find the number position of the cipher by adding the shift 
        cipher_num = (num_in_alphabet + shift) % len(alphabet) 
        # find the cipher letter for the cipher number you computed
        cipher_letter = alphabet[cipher_num] 
        # add the cipher letter to the ciphertext
        ciphertext = ciphertext + cipher_letter 
 
    # return the computed ciphertext
    return ciphertext
