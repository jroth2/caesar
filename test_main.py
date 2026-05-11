import pytest
from main import encrypt_char, encrypt_string, decrypt_char, decrypt_string, parse_args


# --- encrypt_char ---

class TestEncryptChar:
    def test_basic_shift(self):
        assert encrypt_char("A", 1) == "B"

    def test_wrap_around(self):
        assert encrypt_char("Z", 1) == "A"

    def test_shift_13(self):
        assert encrypt_char("A", 13) == "N"

    def test_lowercase(self):
        assert encrypt_char("a", 1) == "b"

    def test_lowercase_wrap(self):
        assert encrypt_char("z", 1) == "a"

    def test_non_alpha_passthrough(self):
        assert encrypt_char(" ", 5) == " "
        assert encrypt_char("!", 5) == "!"
        assert encrypt_char("1", 5) == "1"

    def test_shift_zero(self):
        assert encrypt_char("A", 0) == "A"


# --- decrypt_char ---

class TestDecryptChar:
    def test_basic_shift(self):
        assert decrypt_char("B", 1) == "A"

    def test_wrap_around(self):
        assert decrypt_char("A", 1) == "Z"

    def test_shift_13(self):
        assert decrypt_char("N", 13) == "A"

    def test_lowercase(self):
        assert decrypt_char("b", 1) == "a"

    def test_lowercase_wrap(self):
        assert decrypt_char("a", 1) == "z"

    def test_non_alpha_passthrough(self):
        assert decrypt_char(" ", 5) == " "
        assert decrypt_char("!", 5) == "!"
        assert decrypt_char("1", 5) == "1"


# --- encrypt_string ---

class TestEncryptString:
    def test_simple_word(self):
        assert encrypt_string("ABC", 1) == "BCD"

    def test_wrap_around(self):
        assert encrypt_string("XYZ", 3) == "ABC"

    def test_mixed_case(self):
        assert encrypt_string("aAbB", 1) == "bBcC"

    def test_preserves_spaces(self):
        assert encrypt_string("HELLO WORLD", 1) == "IFMMP XPSME"

    def test_preserves_punctuation(self):
        assert encrypt_string("HI!", 1) == "IJ!"

    def test_empty_string(self):
        assert encrypt_string("", 5) == ""


# --- decrypt_string ---

class TestDecryptString:
    def test_simple_word(self):
        assert decrypt_string("BCD", 1) == "ABC"

    def test_wrap_around(self):
        assert decrypt_string("ABC", 3) == "XYZ"

    def test_mixed_case(self):
        assert decrypt_string("bBcC", 1) == "aAbB"

    def test_preserves_spaces(self):
        assert decrypt_string("IFMMP XPSME", 1) == "HELLO WORLD"

    def test_preserves_punctuation(self):
        assert decrypt_string("IJ!", 1) == "HI!"

    def test_empty_string(self):
        assert decrypt_string("", 5) == ""


# --- round-trip ---

class TestRoundTrip:
    def test_encrypt_then_decrypt(self):
        original = "Hello, World!"
        shift = 7
        assert decrypt_string(encrypt_string(original, shift), shift) == original

    def test_various_shifts(self):
        original = "The Quick Brown Fox"
        for shift in range(1, 26):
            assert decrypt_string(encrypt_string(original, shift), shift) == original


# --- parse_args ---

class TestParseArgs:
    def test_encrypt_flag(self):
        args = parse_args(["hello", "-e"])
        assert args.encrypt is True
        assert args.decrypt is False

    def test_decrypt_flag(self):
        args = parse_args(["hello", "-d"])
        assert args.decrypt is True
        assert args.encrypt is False

    def test_default_shift(self):
        args = parse_args(["hello", "-e"])
        assert args.shift == 1

    def test_custom_shift(self):
        args = parse_args(["hello", "-e", "-s", "13"])
        assert args.shift == 13

    def test_shift_capped_at_charset_length(self):
        args = parse_args(["hello", "-e", "-s", "100"])
        assert args.shift == 26

    def test_file_flag(self):
        args = parse_args(["path/to/file.txt", "-f", "-e"])
        assert args.file is True
        assert args.string == "path/to/file.txt"

    def test_output_flag(self):
        args = parse_args(["hello", "-e", "-o", "out.txt"])
        assert args.output == "out.txt"
