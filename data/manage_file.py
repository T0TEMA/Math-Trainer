"""
Author : Totema

Python file to manage the saved '.txt' files.
"""


def read_file(file: str) -> dict:
    """
    Function that reads and returns '.txt' files in a python dict type structure.
    :param file: A string to a '.txt' file.
    :return: A dict type structure with the data inside.
    """
    return eval(open(file).read())


def write_file(file: str, content: dict) -> None:
    """
    Function that saves program data into a '.txt' file under a python dict format.
    :param file: A string to a '.txt' file.
    :param content: Content to save in the '.txt' file.
    :return: None
    """
    with open(file, 'w') as f:
        f.write('{\n')
        for key, value in content.items():
            f.write(f'"{key}": "{value}",\n')
        f.write('}')


class Settings:
    """
    Class containing all the used settings for the Qt window.
    """
    def __init__(self):
        self.path = "data/settings.txt"
        self.content = read_file(self.path)

    def save(self):
        """
        Calling the write_file function to save data.
        :return: None
        """
        write_file(self.path, self.content)


class UserData:
    """
    Class containing all the used user data for the user profile.
    """
    def __init__(self):
        self.path = "data/userdata.txt"
        self.content = read_file(self.path)

    def save(self):
        """
        Calling the write_file function to save data.
        :return: None
        """
        write_file(self.path, self.content)
