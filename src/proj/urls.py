
from django.contrib import admin
from django.urls import path, include
from forecast import views
import reference


urlpatterns = [
    path('admin/', admin.site.urls),
    path('forecast/', views.show_forecast_view),
    path ('main_page/', views.show_mainpage_view),
    path ('book_page/', views.BookPage.as_view()),
    path('book/<int:id>/', views.BookDetailView.as_view()),
    path ('map_page/', views.MapPage.as_view()),
    #path ('book_add/', views.book_add_view),
    #path ('map_page/', views.BookEdit.as_view()),
    path ('book_add/', views.BookAdd.as_view()),
    path('ref/', include(('reference.urls', 'refernce'), namespace ='ref'))
]
