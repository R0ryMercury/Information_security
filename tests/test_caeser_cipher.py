import pytest
from src.enums.caesar_ciphre_enums import Params
from project.backend.ciphres.caeaser_ciphre import caeser_cipher


@pytest.mark.parametrize("input_string, shift, result", Params.input_encrypted.value)
def test_encode_caesar_ciphre(input_string, shift, result):
    assert caeser_cipher(string=input_string, amount=shift) == result


@pytest.mark.parametrize("input_string, shift, result", Params.input_encrypted.value)
def test_decode_caesar_ciphre(input_string, shift, result):
    assert caeser_cipher(string=input_string, amount=shift, is_shifred=True) == result
