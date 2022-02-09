from core.rest_client import RestClient


class Repos(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Repos, self).__init__(api_root_url, **kwargs)
    def list_your_repos(self, **kwargs):
        # params = {"visibility": visibility, "affiliation": affiliation, "type": type, "direction": direction}
        return self.get("/user/repos", **kwargs)

    def list_user_repos(self, username, **kwargs):
        return self.get("/users/{}/repos".format(username), **kwargs)

    def list_organization_repos(self, org, **kwargs):
        return self.get("/orgs/{}/repos".format(org), **kwargs)

    def list_all_public_repos(self, **kwargs):
        return self.get("/repositories", **kwargs)

    def create_user_repos(self, **kwargs):
        return self.post("/user/repos", **kwargs)

    def create_organization_repos(self, org, **kwargs):
        return self.post("/orgs/{}/repos".format(org), **kwargs)

    def get_repo(self, owner, repo, **kwargs):
        return self.get("/repos/{}/{}".format(owner, repo), **kwargs)

    def edit_repo(self, owner, repo, **kwargs):
        return self.patch("/repos/{}/{}".format(owner, repo), **kwargs)

