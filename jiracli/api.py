from . import auth


class API(object):
    def __init__(self, config):
        self.cfg = config
        self._jira = auth.basic(config.server, username=config.username,
                                password=config.password, unsafe=config.unsafe)

    def list_issues(self):
        query = "project={} and assignee = {} " \
                "and status != 'closed'".format(self.cfg.project, self.cfg.username)
        return self._jira.search_issues(query)

    def issue(self, issue):
        return self._jira.issue(issue)
