import jira
import requests


def basic(server, username, password, unsafe=False):
    """Return a api Connection using basic username/password
    authentication"""
    jira_options = {}
    if unsafe:
        requests.packages.urllib3.disable_warnings()
        jira_options = {
            'verify': False,
            'check_update': False,
        }

    return jira.JIRA(server, options=jira_options, basic_auth=(username, password))