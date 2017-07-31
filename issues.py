#!/usr/bin/env python3
import jira
import requests
import argparse

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


def parse():
    """Return an instance of ArgumentParser with parsed arguments"""
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('username', help="JIRA Username", type=str)
    parser.add_argument('password', help="JIRA Password.", type=str)
    parser.add_argument('project', help="Query project", type=str)
    parser.add_argument('--status', help="Only issues with given status")
    return parser.parse_args()


def main():
    args = parse()
    jira = connection(args.username, args.password)

    query = "project={} and assignee = {} and status != \"closed\" ".format(args.project, args.username)
    all_proj_issues_but_mine = jira.search_issues(query)

    for issue in all_proj_issues_but_mine:
        print("Ticket: {}".format(issue.key))
        print("Summary:{}".format(issue.fields.summary))

if __name__ == '__main__':
    main()




