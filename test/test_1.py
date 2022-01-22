import pytest


def test_foo(test_target, test_param, precondition1):
    assert True


def test_boo(test_target, test_param, precondition1):
    assert True


def test_bar(test_target, test_param, precondition1):
    assert True


def test_mar(test_target, test_param, precondition1):
    assert True


if __name__ == "__main__":
    pytest.main(["-v", "-s"])
