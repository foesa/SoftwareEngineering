from github import Github as gt

curUser = gt("foesa", "Monkeyquest12")

repo = curUser.get_repo("foesa/PortfolioProjects")
commits = repo.get_commits()
for commit in commits:
    stats = commit.stats
    print(stats.additions,stats.deletions,stats.total)