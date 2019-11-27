from siter.models import Commit
from django.core.management.base import BaseCommand
from github import Github as gt



# TODO Maybe put into one function to prevent double iteration through the file.
class Command(BaseCommand):
    help = 'Builds database from CSV file'

    def handle(self, *args, **options):
        token = "88c78ce62a0f702716"
        token = token + "b65eeb2563"
        token = token + "80ab43682eea"
        user = gt("foesa", token)

        repo = user.get_repo("foesa/flask")
        commits = repo.get_commits()
        num = 0
        for commiter in commits:
            statistics = commiter.stats
            _, created = Commit.objects.get_or_create(
                repoName="flask",
                additions=statistics.additions,
                deletions=statistics.deletions,
                total=statistics.total,
                commitDate=commiter.commit.committer.date,
            )
            num = num+1
            print (num)

