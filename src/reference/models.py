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
      return "%i/" % self.id
      

    def death_status(self):
    #"Returns the author's eternity status."
      import datetime
      if self.death_date() < datetime.date(1990, 1, 1):
            return "Classic"
      else:
           return "Contemporary"

class Publisher(models.Model):
    publisher_name = models.CharField(blank=False, max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.publisher_name

    def get_absolute_url(self):
        return "%i/" % self.id

class Seria(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default='Unknown publisher')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
         return self.name

    def get_absolute_url(self):
         return "seria/%i/" % self.id