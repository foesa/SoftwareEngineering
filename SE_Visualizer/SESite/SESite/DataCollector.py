from github import Github as gt

token = "88c78ce62a0f702716"
token = token + "b65eeb2563"
token = token + "80ab43682eea"
user = gt("foesa",token)

repo = user.get_repo("foesa/Django")
commits = repo.get_commits()
print(user.get_rate_limit())
