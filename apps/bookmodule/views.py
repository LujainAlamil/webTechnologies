from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html")

def index2(request, val1 = 0):   
    return HttpResponse("value1 = "+str(val1))

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
 
