import os
import yaml


def parse(path='~/.jira.yml'):
    """Parse api.yml and return the object
    representation of that file"""
    data = yaml.load(open(os.path.expanduser(path)))
    try:
        return Config(username=data['username'], password=data['password'],
                      server=data['server'], project=data['project'], unsafe=data['unsafe'])
    except KeyError:
        print("Cannot parse {}".format(path))


class Config(object):
    def __init__(self, username, password, server, project, unsafe):
        self.username = username
        self.password = password
        self.server = server
        self.project = project
        self.unsafe = unsafe
