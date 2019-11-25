from django.shortcuts import render
from github import Github as gt
# Create your views here.
def inputPage(request):
    return render(request,"inputPage.html")

def searchResults(request):
    users = gt.search_users(request.GET['search'])
    context = {
        'user': users
    }
    return render(request,"searchResults.html",context)

def userDetails(request,user):
    curUser = user
    context = {
        'mainUser' : user
    }
    return render(request,"userDetails.html",context)