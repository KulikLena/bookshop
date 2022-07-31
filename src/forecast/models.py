from random import choices
from django.db import models

class BookInstance(models.Model):
    import datetime
    #There will be placed unique instances of books 
    native_language_book_title = models.CharField(max_length=50)
    first_published = models.DateField(blank=False, default=datetime.date(1990, 1, 1))

    def __str__(self) -> str:
       return self.native_language_book_title


class Author(models.Model):
    import datetime
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=False, default=datetime.date(1, 1, 1))
    death_date = models.DateField(blank=True,null=True)
    country_of_birth = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.first_name+' '+self.last_name 

    #def death_status(self):
        #"Returns the author's eternity status."
      #  import datetime
       # if self.death_date() < datetime.date(1990, 1, 1):
       #     return "Classic"
        #else:
        #    return "Contemporary"


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.publisher_name


class Genre(models.Model):
    #NONFICTION
    ART = 'Art/architecture'
    AUTOBIOGRAPHY = 'Autobiography'
    BIOGRAPHY ='Biography'
    BUSINESS = 'Business'
    CRAFTS = 'Crafts'
    COOKBOOK = 'Cookbook'
    DIARY = 'Diary'
    DICTIONARY = 'Dictionary'
    ENCYCLOPEDIA = 'Encyclopedia'
    GUIDE = 'Guide'
    HEALTH = 'Health'
    HISTORY = 'History'
    HOME = 'Home'
    HUMOR= 'Humor'
    JOURNAL= 'Journal'
    MATH ='MATH'
    MEMOIR = 'Memoir'
    PHILOSOPHY = 'Philosophy'
    PRAYER = 'Prayer'
    RELIGION = 'Religion'
    TEXTBOOK= 'Textbook'
    TRUE_CRIME = 'True crime'
    REVIEW = 'Review'
    SCIENCE = 'Science'
    SELF = 'Self'
    SPORTS = 'Sports'
    TRAVEL = 'Travel' 
    OTHER = 'Other'
    #Fiction
    ACTION = 'Action'
    ALTERNATIVE = 'Alternate history'
    ANTOLOGY = 'Anthology'
    CHIK = 'Chick lit'
    CHILD = 'Childrens'
    CLASSIC = 'Classic'
    COMIC = 'Comic book'
    COMING = 'Coming-of-age'
    CRIME = 'Crime'
    DRAMA = 'Drama'
    FAIRYTALE = 'Fairytale'
    FANTASY = 'Fantasy'
    GRAPHIC = 'Graphic novel'
    HISTORICAL = 'Historical fiction'
    HORROR = 'Mystery'
    MYSTERY = 'Comic book'
    PARANORMAL = 'Paranormal romance'
    PICTURE = 'Picture book'
    POETRY = 'Poetry'
    POLITICAL = 'Political thriller'
    ROMANCE = 'Romance'
    SATIRE = 'Satire'
    SCI_FI = 'Science fiction'
    SHORTS = 'Short story'
    SUSPENSE = 'Suspense'
    THRILLER = 'Thriller'
    WESTERN = 'Thriller'
    YOUNG_ADULT = 'Young adult'
   
    GENRE_CHOICES = [
        ('Nonfiction', (
            (ART,'Art/architecture'), (AUTOBIOGRAPHY,'Autobiography'), (BIOGRAPHY,'Biography'), (BUSINESS, 'Business/economics'),
            (CRAFTS, 'Crafts/hobbies'), (COOKBOOK, 'Cookbook'), (DIARY, 'Diary'), (DICTIONARY,'Dictionary'), 
            (ENCYCLOPEDIA, 'Encyclopedia'), (GUIDE, 'Guide'), (HEALTH, 'Health/fitness'), (HISTORY, 'History'), (HOME, 'Home and garden'),
            (HUMOR, 'Humor'), (JOURNAL, 'Journal'), (MATH, 'Math'), (MEMOIR, 'Memoir'), (PHILOSOPHY, 'Philosophy'),
            (PRAYER,'Prayer'),(RELIGION,'Religion, spirituality, and new age'), (TEXTBOOK,'Textbook'), (TRUE_CRIME,'True crime'),
            (REVIEW, 'Review'), (SCIENCE, 'Science'), (SELF, 'Self help'),
            (SPORTS, 'Sports and leisure'), (TRAVEL, 'Travel'), (OTHER, 'Other')
        )),
    
        ('Fiction', (
            (ACTION,'Action and adventure'),(ALTERNATIVE, 'Alternate history'), (ANTOLOGY, 'Anthology'), (CHIK, 'Chick lit'), 
            (CHILD, 'Childrens'), (CLASSIC, 'Classic'), (COMIC, 'Comic book'), (COMING, 'Coming-of-age'), (CRIME, 'Crime'), 
            (DRAMA, 'Drama'), (FAIRYTALE, 'Fairytale'), (FANTASY, 'Fantasy'), (GRAPHIC, 'Graphic novel'), (HISTORICAL, 'Historical fiction'),
            (HORROR, 'Horror'), (MYSTERY, 'Mystery'), (PARANORMAL, 'Paranormal romance'), (PICTURE, 'Picture book'), (POETRY, 'Poetry'),
            (POLITICAL, 'Political thriller'), (ROMANCE, 'Romance'), (SATIRE, 'Satire'), (SCI_FI, 'Science fiction'), (SHORTS, 'Short story'),
            (SUSPENSE, 'Suspense'), (THRILLER, 'Thriller'),(WESTERN, 'Western'), (YOUNG_ADULT, 'Young adult'), (OTHER, 'Other')
           
        )),
        
        ('unknown', 'Unknown'),
    ]
    genre = models.CharField(
            max_length=20,
            choices=GENRE_CHOICES,
            default=OTHER,
    )
    
class Book(models.Model):
     import datetime
     name = models.CharField(max_length=150)
     genre = models.CharField(choices=Genre.GENRE_CHOICES,max_length=20)
     authors = models.ManyToManyField('Author')
     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
     date_published = models.DateField(blank=False, default=datetime.date(1990, 1, 1))
     description = models.TextField(blank=True, null=True)


     def __str__(self) -> str:
         return self.name