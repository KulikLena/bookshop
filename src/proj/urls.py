
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
    path ('book_search/', views.BookSearch.as_view()),
    path('book/<int:pk>/', views.BookDetailView.as_view()),
    path('/book/<int:pk>/', views.BookDetailView.as_view()),
    path ('main_page/', views.MainPage.as_view()),
    path ('map_page/', views.MapPage.as_view()),
    #path ('book_add/', views.book_add_view),
    #path ('map_page/', views.BookEdit.as_view()),
    path ('book_add/', views.BookAdd.as_view()),
    path ('new_arrivals/', views.NewArrivals.as_view()),
    path ('bestsellers/', views.Bestsellers.as_view()),
    path ('catalogue/', views.Catalogue.as_view()),
    path('ref/', include(('reference.urls', 'reference'), namespace ='ref')),
    path('order/', include('order.urls', namespace ='order')), 
    path ('main_page/thanks/', views.MainPageThanks.as_view()),
   
]
