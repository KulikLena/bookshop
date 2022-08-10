
from django.contrib import admin
from django.urls import path, include
from forecast import views
import reference


urlpatterns = [
    path('admin/', admin.site.urls),
    path('navbar/', views.NavBar.as_view()),
    path('forecast/', views.show_forecast_view),
    path ('main_page/', views.MainPage.as_view()),
    path ('book_list/', views.BookPage.as_view()),
    path('book/<int:pk>/', views.BookDetailView.as_view()),
    path('book_list/book/<int:pk>/', views.BookDetailView.as_view()),
    path ('main_page/', views.MainPage.as_view()),
    path ('map_page/', views.MapPage.as_view()),
    #path ('book_add/', views.book_add_view),
    #path ('map_page/', views.BookEdit.as_view()),
    path ('book_add/', views.BookAdd.as_view()),
    path('ref/', include(('reference.urls', 'reference'), namespace ='ref'))
]
