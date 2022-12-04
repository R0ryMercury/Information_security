from string import ascii_lowercase, ascii_uppercase


def caeser_cipher(string: str, amount: int, is_shifred=False) -> str:
    """Функция, шифрующая и дешифрующая строку с помощью шифра цезаря"""
    if is_shifred:
        shifted: str = ascii_lowercase[-amount % 26 :] + ascii_lowercase[: -amount % 26]
        translation: dict = str.maketrans(
            shifted + shifted.upper(), ascii_lowercase + ascii_uppercase
        )
    else:
        shifted: str = ascii_lowercase[amount % 26 :] + ascii_lowercase[: amount % 26]
        translation: dict[int, int | None] = str.maketrans(
            ascii_lowercase + ascii_uppercase, shifted + shifted.upper()
        )

    return string.translate(translation)
