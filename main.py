CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    print(encrypt_char("A",26))
    

def encrypt_char(input_char,shift=1):
    for index,char in enumerate(CHARSET):
        if char==input_char:
            input_char_index = index
        else:
            # character not in charset (i.e. ! # $)
        return char

    if input_char_index + shift >= len(CHARSET):
        shifted_index = (input_char_index + shift) - len(CHARSET)
    else:
        shifted_index = input_char_index+shift
    output_char = CHARSET[shifted_index]
    return output_char

    
### 
# Z - charset[25] -> A - charset[0]



if __name__ == "__main__":
    main()
