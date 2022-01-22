import pytest
import yaml


def load_station(devices_file, sut_name):
    with open(devices_file, "r") as file:
        setups = yaml.safe_load(file)
    sut = setups.get(sut_name)
    if not sut:
        pytest.exit(
            f"{sut_name} configuration not found\
                        on file {devices_file}"
        )
    return sut


def pytest_configure(config):
    devices_file = "station.yaml"
    sut_name = "my_station"
    pytest.my_station = load_station(devices_file, sut_name)
