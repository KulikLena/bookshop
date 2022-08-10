from django.db import models

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

    def get_absolute_url(self):
      return f'ref/auth/add/{self.pk}/'

class Publisher(models.Model):
    publisher_name = models.CharField(blank=False, max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.publisher_name

    def get_absolute_url(self):
      return f'ref/pub/add/{self.pk}/'

class Seria(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default='Unknown publisher')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
         return self.name

    def get_absolute_url(self):
      return f'ref/pub/add/{self.pk}/'