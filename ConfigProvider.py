from configparser import ConfigParser

configparser = ConfigParser()
configparser.read('config.ini')


class ConfigProvider:

    @staticmethod
    def get_server_property(config_name: str):
        return configparser.get('minecraft.server', config_name)

    @staticmethod
    def get_client_property(config_name: str):
        return configparser.get('minecraft.client', config_name)
