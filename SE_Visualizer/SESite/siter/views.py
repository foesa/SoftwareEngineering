from django.shortcuts import render
from github import Github as gt
# Create your views here.
def inputPage(request):
    return render(request,"inputPage.html")

def userDetails(request):
    querys = request.GET['search']
    print(querys)
    curUser = gt("foesa", "a787d810507b0aa1100d22410701d9308e347c51")
    users = curUser.search_users(str(querys)+" in:login")
    curUser = users[0]
    context = {
        'mainUser' :curUser
    }
    return render(request,"userDetails.html",context)