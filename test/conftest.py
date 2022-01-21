import time
import json
import pytest
import yaml


def pytest_generate_tests(metafunc):
    # devices_file = metafunc.config.getoption("devices_file")
    devices_file = "station.yaml"
    sut_name = "my_station"
    with open(devices_file) as file:
        # content = file.read()

        # content = '{"my_station": {"target1": 12345, "param1": 67890}}'
        # setups = json.loads(content)

        setups = yaml.safe_load(file)
        # setups = setups1.copy()
    setups = {
        "my_station": {
            "target1": 12345,
            "param1": 67890,
        }
    }
    sut = setups.get(sut_name)
    if not sut:
        pytest.exit(
            f"{sut_name} configuration not found\
                        on file {devices_file}"
        )
    targets = [device for device in sut if device.startswith("target")]
    params = [device for device in sut if device.startswith("param")]
    if "test_target" in metafunc.fixturenames:
        metafunc.parametrize("test_target", targets, scope="module")
    if "test_param" in metafunc.fixturenames:
        metafunc.parametrize("test_param", params, scope="module")


# @pytest.fixture(scope="session")
# def sut():
#     devices_file = "station.yaml"
#     sut_name = "my_station"
#     with open(devices_file) as file:
#         setups = yaml.safe_load(file)
#     sut = setups.get(sut_name)
#     return sut


# @pytest.fixture(scope="module")
# def test_target_number(sut, test_target):
#     return sut.get(test_target)


# @pytest.fixture(scope="module")
# def test_param_number(sut, test_param):
#     return sut.get(test_param)


# @pytest.fixture(scope="module", autouse=True)
# def precondition1(test_target):
#     print("\nStart precondition1 \nSave current status of test target")
#     yield
#     time.sleep(0.1)
#     print("\nStop precondition1 \nRestore original status of test target")
