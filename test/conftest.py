import time
import json
import pytest
import yaml


def pytest_generate_tests(metafunc):
    devices_file = "station.yaml"
    sut_name = "my_station"
    with open(devices_file,"r") as file:
        setups = yaml.safe_load(file)
        # setups = json.load(file)
    # setups = {
    #     "my_station": {
    #         "target1": 12345,
    #         "param1": 67890,
    #     }
    # }
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


@pytest.fixture(scope="module", autouse=True)
def precondition1(test_target):
    print(f"\nStart precondition1 \nSave current status of test target {test_target}")
    yield
    time.sleep(0.1)
    print(f"\nStop precondition1 \nRestore original status of test target {test_target}")
