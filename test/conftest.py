import time
import pytest


def pytest_generate_tests(metafunc):
    sut = pytest.my_station
    targets = [device for device in sut if device.startswith("target")]
    params = [device for device in sut if device.startswith("param")]
    if "test_target" in metafunc.fixturenames:
        metafunc.parametrize("test_target", targets, scope="module")
    if "test_param" in metafunc.fixturenames:
        metafunc.parametrize("test_param", params, scope="module")


@pytest.fixture(scope="module")
def precondition1(test_target):
    print(f"\nStart precondition1 \nSave current status of test target {test_target}")
    yield
    time.sleep(0.1)
    print(
        f"\nStop precondition1 \nRestore original status of test target {test_target}"
    )
