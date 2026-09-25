from validate_b import validate_email


def test_validate_email_accepts_normal_address():
    assert validate_email("person@example.com") is True


def test_validate_email_rejects_address_missing_dot():
    assert validate_email("person@example") is False


def test_validate_email_accepts_subdomain_address():
    assert validate_email("person@mail.example.com") is True


def test_validate_email_rejects_300_character_address():
    address = "a" * 288 + "@example.com"

    assert len(address) == 300
    assert validate_email(address) is False
