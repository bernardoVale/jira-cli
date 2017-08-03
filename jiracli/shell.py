import cmd
import jinja2

class Jira(cmd.Cmd):
    intro = 'Welcome to JIRA interactive shell. Type help or ? to list commands.\n'
    prompt = 'jiracli>'

    def __init__(self, api):
        super().__init__()
        self.api = api

    def do_issues(self, arg):
        'List all non closed issues assigned to your username'
        for issue in self.api.list_issues():
            print("{} - {}".format(issue.key, issue.fields.summary))

    def do_describe(self, arg):
        'Describe issue'
        issue = self.api.issue(arg.upper())

        content = open('templates/describe.j2').read()
        template = jinja2.Template(content)
        print(template.render(name=issue.key, summary=issue.fields.summary,
                              description=issue.fields.description,
                              tab=' ' * 10,
                              status=issue.fields.status, resolution=issue.fields.resolution,
                              type=issue.fields.issuetype, priority=issue.fields.priority))

    def do_set_project(self, arg):
        'Define JIRA project that you\'re working on. All subsequent queries will use this project by default'
        self.api.cfg.project = arg.upper()

    def do_set_user(self, arg):
        'Define a different JIRA user.'
        self.api.cfg.username = arg.lower()

    @staticmethod
    def do_exit(arg):
        'Exit JIRA interactive shell. subsequent queries will use this project by default'
        return True
