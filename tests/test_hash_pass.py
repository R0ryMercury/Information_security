from project.backend.helpers import check_password, get_hashed_password


def test_hash():
    hash_pass = get_hashed_password("1234")
    assert check_password(hashed_password=hash_pass, password="1234")
