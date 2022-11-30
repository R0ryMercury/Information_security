import pytest

from project.backend.ciphres.caeaser_ciphre import caeser_cipher

test_input_encrypted = [
    ("a", 0, "a"),
    ("a", 1, "b"),
    ("a", 26, "a"),
    ("m", 13, "z"),
    ("n", 13, "a"),
    ("OMG", 5, "TRL"),
    ("O M G", 5, "T R L"),
    ("Testing 1 2 3 testing", 4, "Xiwxmrk 1 2 3 xiwxmrk"),
    ("Let's eat, Grandma!", 21, "Gzo'n zvo, Bmviyhv!"),
    (
        "The quick brown fox jumps over the lazy dog.",
        13,
        "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",
    ),
]
test_input_decrypted = [
    ("a", 0, "a"),
    ("b", 1, "a"),
    ("a", 26, "a"),
    ("z", 13, "m"),
    ("a", 13, "n"),
    ("TRL", 5, "OMG"),
    ("T R L", 5, "O M G"),
    ("Xiwxmrk 1 2 3 xiwxmrk", 4, "Testing 1 2 3 testing"),
    ("Gzo'n zvo, Bmviyhv!", 21, "Let's eat, Grandma!"),
    (
        "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",
        13,
        "The quick brown fox jumps over the lazy dog.",
    ),
]


class TestCaeserCipher:
    def test_shift_a_by_0_same_output_as_input(self):

        assert caeser_cipher("a", 0) == "a"

    def test_shift_a_by_1(self):
        assert caeser_cipher("a", 1) == "b"

    def test_shift_a_by_26_same_output_as_input(self):
        assert caeser_cipher("a", 26) == "a"

    def test_shift_m_by_13(self):
        assert caeser_cipher("m", 13) == "z"

    def test_shift_n_by_13_with_wrap_around_alphabet(self):
        assert caeser_cipher("n", 13) == "a"

    def test_shift_capital_letters(self):
        assert caeser_cipher("OMG", 5) == "TRL"

    def test_shift_spaces(self):
        assert caeser_cipher("O M G", 5) == "T R L"

    def test_shift_numbers(self):
        assert caeser_cipher("Testing 1 2 3 testing", 4) == "Xiwxmrk 1 2 3 xiwxmrk"

    def test_shift_punctuation(self):
        assert caeser_cipher("Let's eat, Grandma!", 21) == "Gzo'n zvo, Bmviyhv!"

    def test_shift_all_letters(self):
        assert (
            caeser_cipher("The quick brown fox jumps over the lazy dog.", 13)
            == "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
        )

    def test_shift_a_by_0_same_output_as_input_(self):

        assert caeser_cipher("a", 0, True) == "a"

    def test_shift_a_by_1_(self):
        assert caeser_cipher("b", 1, True) == "a"

    def test_shift_a_by_26_same_output_as_input_(self):
        assert caeser_cipher("a", 26, True) == "a"

    def test_shift_m_by_13_(self):
        assert caeser_cipher("z", 13, True) == "m"

    def test_shift_n_by_13_with_wrap_around_alphabet_(self):
        assert caeser_cipher("a", 13, True) == "n"

    def test_shift_capital_letters_(self):
        assert caeser_cipher("TRL", 5, True) == "OMG"

    def test_shift_spaces_(self):
        assert caeser_cipher("T R L", 5, True) == "O M G"

    def test_shift_numbers_(self):
        assert (
            caeser_cipher("Xiwxmrk 1 2 3 xiwxmrk", 4, True) == "Testing 1 2 3 testing"
        )

    def test_shift_punctuation_(self):
        assert caeser_cipher("Gzo'n zvo, Bmviyhv!", 21, True) == "Let's eat, Grandma!"

    def test_shift_all_letters_(self):
        assert (
            caeser_cipher("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.", 13, True)
            == "The quick brown fox jumps over the lazy dog."
        )
