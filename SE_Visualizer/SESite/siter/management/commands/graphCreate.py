import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from django.core.management.base import BaseCommand
from siter.models import Commit

class Command(BaseCommand):
    help = 'Creates Images'

    def handle(self, *args, **options):
        commitList = Commit.objects.filter(repoName='Django')
        dateList = []
        totalList = []
        for i in commitList:
            if i.additions<50 and i.deletions <50:
                dateList.append(i.deletions)
                totalList.append(i.additions)
        commitList2 = Commit.objects.filter(repoName='flask')
        print(dateList)
        print(totalList)
        scatter1 = plt.scatter(dateList, totalList, s =1, c = 'blue')
        scatter1.figure.savefig("djangoScatter.png")