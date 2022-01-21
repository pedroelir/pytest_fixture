import time
import pytest


def test_foo(test_target, test_param, precondition1):
    assert True


def test_boo(test_target, test_param, precondition1):
    assert True


def test_bar(test_target, test_param, precondition1):
    assert True


def test_mar(test_target, test_param, precondition1):
    assert True


@pytest.fixture(scope="module", autouse=True)
def precondition1(test_target):
    print("\nStart precondition1 \nSave current status of test target")
    yield
    time.sleep(0.1)
    print("\nStop precondition1 \nRestore original status of test target")
