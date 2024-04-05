import unittest

import ServerAccessor
from ConfigProvider import ConfigProvider


class MyTestCase(unittest.TestCase):
    def test_connection(self):
        server_accesor = ServerAccessor.ServerAccessor(ConfigProvider.get_server_property("serverip"),
                                                       ConfigProvider.get_server_property("user"),
                                                       ConfigProvider.get_server_property("sslkey"))
        assert server_accesor is not None

        result = server_accesor.run("ls -la")
        assert result is not None
        print(result)

        result = server_accesor.read_files()
        assert result is not None
        print(result)

        server_accesor.close()


if __name__ == '__main__':
    unittest.main()
