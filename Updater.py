import datetime
from datetime import datetime


from ClientAccessor import ClientAccessor
from ConfigProvider import ConfigProvider
from MinecraftModComparator import MinecraftModComparator
from ServerAccessor import ServerAccessor


def print_upload_status(current_bytes: int, total_bytes: int):
    Updater.start_time = datetime.now()
    if Updater.start_time.second % 5 == 0 | current_bytes == total_bytes:
        convert_bytes(current_bytes, total_bytes)


def convert_bytes(current_bytes: int, total_bytes: int):
    """
    Converts bytes to megabytes and prints the result in the format "current_bytes/total_bytes MB".

    Args:
        current_bytes: The current number of bytes.
        total_bytes: The total number of bytes.
    """
    mb_conversion = 1024 * 1024
    current_mb = current_bytes / mb_conversion
    total_mb = total_bytes / mb_conversion
    print(f"{current_mb:.2f}/{total_mb:.2f} MB for {Updater.current_modname}")


class Updater:
    current_modname = ""
    start_time = datetime.now()

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
                        Updater.current_modname = client_mod
                        Updater.start_time = datetime.now()
                        self.server_accessor.upload(self.client_accessor.get_absolute_path(client_mod),
                                                    client_mod,
                                                    print_upload_status)
                        # After mod is found we don't need to search further
                        break
        self.server_accessor.close()
