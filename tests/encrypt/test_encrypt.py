from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "5")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(5, 6)

    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("test", 4) == "tset"
