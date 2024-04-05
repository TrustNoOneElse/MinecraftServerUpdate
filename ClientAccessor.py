import os

from ConfigProvider import ConfigProvider


class ClientAccessor:
    def __init__(self):
        self.mod_directory = ConfigProvider.get_client_property("modsdir")

    def list_files_in_directory(self):
        file_names = []
        # Iterate over all files in the directory
        for file_name in os.listdir(self.mod_directory):
            # Check if the item is a file (not a directory)
            if os.path.isfile(os.path.join(self.mod_directory, file_name)):
                file_names.append(file_name)
        return file_names

    def get_absolute_path(self, file_name: str):
        return os.path.join(self.mod_directory, file_name)


