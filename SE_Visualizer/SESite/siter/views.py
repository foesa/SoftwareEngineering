from django.shortcuts import render
from github import Github as gt
# Create your views here.

def inputPage(request):

    return render(request,"inputPage.html")

def userDetails(request):
    querys = request.GET['search']
    print(querys)
    token = "88c78ce62a0f702716"
    token = token + "b65eeb2563"
    token = token + "80ab43682eea"
    curUser = gt("foesa", token)
    users = curUser.search_users(str(querys)+" in:login")
    curUser = users[0]
    context = {
        'mainUser' :curUser
    }
    return render(request,"userDetails.html",context)