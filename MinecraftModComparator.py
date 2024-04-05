import re


class MinecraftModComparator:

    @staticmethod
    def compare_mods(mod1: str, mod2: str):
        name_mod1 = MinecraftModComparator.extract_mod_name(mod1)
        name_mod2 = MinecraftModComparator.extract_mod_name(mod2)
        return name_mod1 == name_mod2

    @staticmethod
    def extract_mod_name(mod_filename: str):
        # Remove version numbers and file extensions from the filename
        mod_name = re.sub(r'[\d.-]', '', mod_filename.split('.')[0])
        return mod_name
