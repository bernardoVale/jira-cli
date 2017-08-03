#!/usr/bin/env python3
import argparse
from jiracli import connection

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




