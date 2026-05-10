import argparse


CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    args = parse_args()
    print(encrypt_string(args.string,args.shift))

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Encrypt one or more characters using a Caesar shift."
    )
    parser.add_argument(
        "string",
        help="A string to be encoded or decoded"

    )
    parser.add_argument(
        "shift",
        type=int,
        default=1,
        help="Cipher offset to apply from 1-25 (default: 1).",
    )

    args = parser.parse_args(argv)
    if args.shift > len(CHARSET):
        args.shift = len(CHARSET)

    return args



def encrypt_char(input_char,shift):

    for index,char in enumerate(CHARSET):
        if char==input_char:
            input_char_index = index

            # if the shift + index is greater than the length of charset, wrap around the index to the start of charset
            if input_char_index + shift >= len(CHARSET):
                shifted_index = (input_char_index + shift) - len(CHARSET)
            else:
                shifted_index = input_char_index+shift
            output_char = CHARSET[shifted_index]
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
