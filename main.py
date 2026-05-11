import argparse


CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    args = parse_args()
    if args.file:
        with open(args.string,"r") as f:
            input_str = f.read()
        if args.encrypt:
            print(encrypt_string(input_str,args.shift))
        elif args.decrypt:
            print("not yet implemented")

    elif args.encrypt:
        print(encrypt_string(args.string,args.shift))
    elif args.decrypt:
        print("not yet implemented")
    

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Encrypt one or more characters using a Caesar shift.")

    parser.add_argument("string",help="A string to be encoded or decoded")
    parser.add_argument("-f", "--file", action="store_true", help="When added, the string argument is treated as a file path to read the string from.")
    parser.add_argument("-e", "--encrypt",action="store_true", help="Sets script to encrypt")
    parser.add_argument("-d", "--decrypt",action="store_true", help="Sets script to decrypt")
    parser.add_argument("-s", "--shift", type=int, default=1, help="Cipher offset to apply from 1-25 (default: 1).")

    args = parser.parse_args(argv)
    if args.shift > len(CHARSET):
        args.shift = len(CHARSET)

    print(args)

    return args



def encrypt_char(input_char,shift):
    if input_char.islower():
        charset = CHARSET.lower()
    else:
        charset = CHARSET
        

    for index,char in enumerate(charset):
        if char==input_char:
            input_char_index = index

            # if the shift + index is greater than the length of charset, wrap around the index to the start of charset
            if input_char_index + shift >= len(charset):
                shifted_index = (input_char_index + shift) - len(charset)
            else:
                shifted_index = input_char_index+shift
            output_char = charset[shifted_index]
            return output_char
    # only runs if no match in charset
    return input_char

def encrypt_string(input_str,shift):
    output_list = []
    for char in input_str:
        output_list.append(encrypt_char(char,shift))
    return "".join(output_list)

if __name__ == "__main__":
    main()
