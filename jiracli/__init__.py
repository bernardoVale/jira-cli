from . import auth
from . import config
from .api import API
from . import shell

__version__ = '0.1'


def main():
    _api = API(config.parse())
    shell.Jira(_api).cmdloop()
