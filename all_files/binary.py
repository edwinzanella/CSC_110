def bin_to_dec(binary):
    final = 0
    for i in range(len(binary)):
        amount = len(binary) - i
        integer = str(i) ** amount
        final = final + integer
    return final
