from api.reposiories.repos import Repos


class Github:
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)


if __name__ == '__main__':
    r = Github(token="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")
    username = "1028768918"
    orgnname = "collectiveidea"
    # x = r.repos.list_your_repos()
    # print(x.text)

    # case 1
    data = {
        "name": "Hello-World21",
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }

    # case 1
    x = r.repos.create_user_repos(json=data)
    print(x.status_code)
    assert x.status_code == 422

    # case 2
    x = r.repos.create_organization_repos(orgnname, json=data)
    print(x.status_code)
    assert x.status_code == 403

    # case 3
    x = r.repos.get_repo(username, "Hello-World21")
    print(x.status_code)
    assert x.status_code == 200
    print(x.text)

    # case 4
    data = {
        "name": "Hello-World22",
        "description": "2022:This is first repository",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_project": True,
        "has_wiki": True
    }
    x = r.repos.edit_repo(username, "Hello-World21", json=data)
    print(x.status_code)
    print(x.text)
    assert x.status_code == 200

    """
    x = r.repos.list_your_repos(visibility="private")
    print(x.text)

    x = r.repos.list_your_repos(visibility="all")
    print(x.text)

    x = r.repos.list_your_repos(direction="desc")
    print(x.text)

    r = Github(username="1028768918", password="bmx199012")
    x = r.repos.list_your_repos()
    print(x.text)

    # data = {"direction": "desc"}
    # x = r.repos.list_user_repos("1028768918", params=data)
    # print(x.text)

    data = {"direction": "desc"}
    x = r.repos.list_organization_repos("collectiveidea", params=data)
    print(x.text)

    x = r.repos.list_all_public_repos()
    print(x.text)

    data = {"since": "364"}
    x = r.repos.list_all_public_repos(param=data)
    print(x.text)
    """
