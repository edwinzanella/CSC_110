# Function to convert a binary string to a decimal number

def bin_to_dec(binary):
    # The highest power of 2 will be the length - 1
    high_power = len(binary) - 1
    # Initialize counter at highest power to count down
    i = high_power
    # Initialize accumulator to compute decimal number
    decimal = 0
    # Loop while i is greater than 0
    while i >= 0:
        # If the current character is a 1
        if binary[i] == '1':
            # Compute the power of 2 to add
            power = high_power - i
            # Add the power of two to the decimal accumulator
            decimal = decimal + 2**power
        # Decrement the counter
        i = i - 1
    # Return the decimal accumulator
    return decimal                          

# Function to look up the ASCII representation of a capital letter 
def ascii_lookup(ch):
    if ch == 'A':
        return "01000001"
    elif ch == 'B':
        return "01000010"
    elif ch == 'C':
        return "01000011"
    elif ch == 'D':
        return "01000100"
    elif ch == 'E':
        return "01000101"
    elif ch == 'F':
        return "01000110"
    elif ch == 'G':
        return "01000111"
    elif ch == 'H':
        return "01001000"
    elif ch == 'I':
        return "01001001"
    elif ch == 'J':
        return "01001010"
    elif ch == 'K':
        return "01001011"
    elif ch == 'L':
        return "01001100"
    elif ch == 'M':
        return "01001101"
    elif ch == 'N':
        return "01001110"
    elif ch == 'O':
        return "01001111"
    elif ch == 'P':
        return "01010000"
    elif ch == 'Q':
        return "01010001"
    elif ch == 'R':
        return "01010010"
    elif ch == 'S':
        return "01010011"
    elif ch == 'T':
        return "01010100"
    elif ch == 'U':
        return "01010101"
    elif ch == 'V':
        return "01010110"
    elif ch == 'W':
        return "01010111"
    elif ch == 'X':
        return "01011000"
    elif ch == 'Y':
        return "01011001"
    elif ch == 'Z':
        return "01011010"
    elif ch == ' ':
        return "00100000"
        

# Function to compute the 8-bit checksum for a string
def checksum8(string):
    # fill in the code to compute the 8-bit checksum
    checksum = 0
    for char in string:
        ascii = ascii_lookup(char)
        dec = bin_to_dec(ascii)
        checksum += dec
        checksum = checksum % 256
    return checksum




# Main Function
def main():
    chString = input("Enter the text for which you would like the checksum computed: ")

    print("Checksum = ",checksum8(chString))
        
        
