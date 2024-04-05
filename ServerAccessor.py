import ConfigProvider

from fabric import Connection
from paramiko import SFTPClient

from ConfigProvider import ConfigProvider


class ServerAccessor:

    def __init__(self, server, user, ssl_path):
        self.server = server
        self.user = user
        self.ssl_path = ssl_path
        self.connection = Connection(self.server, user=self.user, connect_kwargs={
            "key_filename": self.ssl_path
        })
        self.sftp_client = self.open_sftp()
        self.sftp_client.chdir(ConfigProvider.get_server_property("modsdir"))

    # run command
    def run(self, command: str):
        result = self.connection.run(command)
        return result

    def open_sftp(self) -> SFTPClient:
        return self.connection.sftp()

    # upload file or directory
    def upload(self, local_path: str, remote_path: str):
        self.sftp_client.put(local_path, remote_path)

    def read_files(self, path: str = '.'):
        return self.sftp_client.listdir(path)

    # delete file
    def delete(self, path: str):
        self.sftp_client.remove(path)

    def close(self):
        self.connection.close()
        self.sftp_client.close()
