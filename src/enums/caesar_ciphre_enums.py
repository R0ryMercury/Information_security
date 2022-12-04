from enum import Enum


class Params(Enum):
    input_encrypted = [
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

    input_decrypted = [
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
