import os
from configparser import SafeConfigParser


def get_config_value(module, variable):
    _curr_path = os.getcwd()
    _config_path = os.path.join(_curr_path, 'config/config.ini')
    _conf_value = None
    try:
        _parser = SafeConfigParser()
        print(_config_path)
        _parser.read(_config_path)
        _conf_value = _parser.get(module, variable)
    except Exception as e:
        print(str(e))
    finally:
        return _conf_value