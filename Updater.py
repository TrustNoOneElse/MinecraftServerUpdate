from ClientAccessor import ClientAccessor
from ConfigProvider import ConfigProvider
from MinecraftModComparator import MinecraftModComparator
from ServerAccessor import ServerAccessor


class Updater:
    def __init__(self):
        self.server_accessor = ServerAccessor(ConfigProvider.get_server_property("serverip"),
                                              ConfigProvider.get_server_property("user"),
                                              ConfigProvider.get_server_property("sslkey"))
        self.client_accessor = ClientAccessor()

    def start(self):
        server_mods = self.server_accessor.read_files()
        client_mods = self.client_accessor.list_files_in_directory()

        for client_mod in client_mods:
            if client_mod not in server_mods:
                for server_mod in server_mods:
                    if MinecraftModComparator.compare_mods(client_mod, server_mod):
                        print("Updating " + server_mod + " to " + client_mod)
                        # TODO could be parallel
                        self.server_accessor.delete(server_mod)
                        self.server_accessor.upload(self.client_accessor.get_absolute_path(client_mod), client_mod)
                        # After mod is found we don't need to search further
                        break
