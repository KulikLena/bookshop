from django.shortcuts import render, HttpResponse
from random import randint
from . import models 
# Create your views here.
def show_forecast_view(request):
    NAMES = (request.user, 'Nik', 'Mike', 'Rosenkranz', 'Güldenstern') 
    username=NAMES[randint(0,4)]
    PREDICTIONS =('The night is dark and full of terrors','So long, and thanks for all the fish', 
                   'Don_t Panic', 'Something is rotten in the state of Denmark')
    forecast=PREDICTIONS[randint(0,3)]
    return HttpResponse (f"<h1>{forecast}, {username} </h1>")

def show_mainpage_view(request):
    out='<ul>'
    books=models.Book.objects.all()
    for bk in books: 
        out += f"<li> Book {bk.native_language_book_title} </li>"
    out='</ul>'
    return HttpResponse(out)
   