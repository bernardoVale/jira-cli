#!/usr/bin/env python3
import argparse
import cmd
import jinja2
from jiracli import connection

class JiraShell(cmd.Cmd):
    intro = 'Welcome to JIRA interactive shell. Type help or ? to list commands.\n'
    prompt = 'jira>'

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.jira = connection(username, password)


    def do_issues(self, arg):
        'List all non closed issues assigned to your username'
        query = "project={} and assignee = {} and status != 'closed'".format(self.project, self.username)
        for issue in self.jira.search_issues(query):
            print("{} - {}".format(issue.key, issue.fields.summary))

    def do_describe(self, arg):
        'Describe issue'
        issue = self.jira.issue(arg.upper())

        content = open('templates/describe.j2').read()
        template = jinja2.Template(content)
        print(template.render(name=issue.key, summary=issue.fields.summary,
                        description=issue.fields.description,
                        tab=' '*10,
                        status=issue.fields.status, resolution=issue.fields.resolution,
                        type=issue.fields.issuetype, priority=issue.fields.priority))

    def do_set_project(self, arg):
        'Define JIRA project that you\'re working on. All subsequent queries will use this project by default'
        self.project = arg.upper()

    def do_set_user(self, arg):
        'Define a different JIRA user.'
        self.username = arg.lower()

    def do_exit(self, arg):
        'Exit JIRA interactive shell. subsequent queries will use this project by default'
        return True


def parse():
    """Return an instance of ArgumentParser with parsed arguments"""
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('username', help="JIRA Username", type=str)
    parser.add_argument('password', help="JIRA Password.", type=str)
    return parser.parse_args()


def main():
    args = parse()
    args.password = 'wsi1029QWE#'
    JiraShell(username=args.username, password=args.password).cmdloop()

if __name__ == '__main__':
    main()




