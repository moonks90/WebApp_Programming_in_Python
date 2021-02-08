from django.shortcuts import render


# Create your views here.
def home(request):
    data = dict()
    return render(request,"home.html",context=data)


def testpage(request):
    data = dict()
    return render(request,"testpage.html",context=data)


def printnamepage(request):
    data = dict()
    user = request.GET['name']
    data['name'] = user
    return render(request,"printname.html",context=data)
