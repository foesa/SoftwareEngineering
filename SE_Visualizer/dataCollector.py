from github import Github as gt

curUser = gt("foesa", "Monkeyquest12")

for repo in curUser.get_user().get_repos():
    print(repo.name)
