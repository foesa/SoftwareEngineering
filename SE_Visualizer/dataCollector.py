from github import Github as gt
import time
curUser = gt("foesa", "Monkeyquest12")

repo = curUser.get_repo("foesa/Django")
commits = repo.get_commits()
rate = curUser.get_rate_limit().core.remaining
count = 0
username = "maibrahi"
users=curUser.search_users(str(username)+" in:login")
for user in users:
    print(user)