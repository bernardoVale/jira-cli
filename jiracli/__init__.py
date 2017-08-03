from . import auth
from . import config
from . import shell

__version__ = '0.1'


def main():
    cfg = config.parse()
    api = auth.basic(cfg.server, username=cfg.username, password=cfg.password, unsafe=cfg.unsafe)
    shell.Jira(cfg, api).cmdloop()