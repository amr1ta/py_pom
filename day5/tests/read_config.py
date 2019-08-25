from configparser import ConfigParser
from pathlib import Path

def read_configfile(configFileName, configSection, configParam):
    config = ConfigParser()
    base_path = Path(__file__).parent
    configFilePath = (base_path / configFileName).resolve()
    config.read(configFilePath)
    return config.get(configSection, configParam)
