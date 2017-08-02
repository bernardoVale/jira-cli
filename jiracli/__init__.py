import jira
import requests

JIRA_SERVER_URI = 'https://jira.wsgc.com'


def connection(username, password):
    """Return a jira Connection"""
    requests.packages.urllib3.disable_warnings()
    jira_options = {
        # Python doesn't know about WSGC-RootCA, and our cert currently doesn't identify a
        # subjectAltName; one day we will want to make our cert good and tell Python about it, but
        # until then don't verify the host.
        'verify': False,

        # Disable phone-home version check.
        'check_update': False,
    }
    return jira.JIRA(JIRA_SERVER_URI, options=jira_options, basic_auth=(username, password))