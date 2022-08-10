from datetime import datetime
from random import choices
from django.db import models
from django.utils import timezone
from reference.models import Publisher, Author, Seria

ACTIVE= 'Active'
INACTIVE= 'Inactive'

 
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
    def __str__(self) -> str:
         return self.genre

class Cover(models.Model):
    HARD = 'Hard cover'
    SOFT = 'Soft cover'
    OTHER = 'Other cover'
    COVER_CHOICES = [(HARD,'Hard cover'),
            (SOFT,'Soft cover'),
            (OTHER, 'Other')]

    cover = models.CharField(
            max_length=20,
            choices=COVER_CHOICES,
            default=OTHER,
    )
    
    def __str__(self) -> str:
         return self.cover

class AgeRestriction (models.Model):
    NOT_RESTRICTED = 'Without restrictions' 
    ADULT = '18+'
    TEENS = '12+'
    KIDS = '6+'
    TODDLERS = '1+'
    AGE_RESTRICT_CHOICES = [
            (NOT_RESTRICTED,'Without restrictions'),
            (ADULT,'18+'),
            (TEENS, '12+'),
            (KIDS, '6+'),
            (TODDLERS,'1+')]

    age_restriction = models.CharField(
            max_length=20,
            choices=AGE_RESTRICT_CHOICES,
            default=ADULT,
    )
    
    def __str__(self) -> str:
         return self.age_restriction


class Book(models.Model):
     import datetime
     name = models.CharField(max_length=150)
     authors = models.ManyToManyField('reference.Author', default='an author')
     price=models.DecimalField(blank=False, default=10.00, decimal_places=2, max_digits=8)
     genre = models.CharField(choices=Genre.GENRE_CHOICES,max_length=120)
     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
     #seria=models.ForeignKey(Seria, on_delete=models.CASCADE, blank=True, null=True, default='a seria')
     pages = models.IntegerField(blank=False, default=0)
     cover = models.CharField(choices=Cover.COVER_CHOICES, max_length=120, default='Other')
     format = models.CharField(help_text="Please use the following format: width(cm) x length(cm): ",max_length=5, blank=True, null=True)
     date_published = models.DateField(blank=False, default=datetime.date(1990, 1, 1))
     isbn = models.CharField(max_length=40, default='000-000-0000-00-0')
     weight = models.IntegerField(max_length=40, default='0')
     age_restriction = models.CharField(choices=AgeRestriction.AGE_RESTRICT_CHOICES, max_length=402, default='18+')
     items_available = models.IntegerField(blank=False, default=0)
     order_status = models.CharField(choices=[(ACTIVE,'Active'), (INACTIVE,'Inactive')], max_length=40, default='Inactive')
     rate = models.DecimalField(decimal_places=2, max_digits= 3, blank=True, null=True)
     created = models.DateTimeField(editable=False, default=datetime.datetime.now())
     modified = models.DateTimeField(default=datetime.datetime.now())
     description = models.TextField(blank=True, null=True)

     def save(self, *args, **kwargs):
        import datetime
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(Book, self).save(*args, **kwargs)


     def __str__(self) -> str:
         return self.name
    
     def get_absolute_url(self):
         return f'book/{self.pk}/'


