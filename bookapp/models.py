from django.db import models

# Create your models here.
class Author (models.Model):
    a_name = models.CharField(db_index=True,max_length=200)
    a_year = models.CharField(max_length=50)
    def __str__(self):
        return self.a_name

class Publisher (models.Model):
    p_name = models.CharField(db_index=True,max_length=200)
    def __str__(self):
        return self.p_name

class Bookwriter (models.Model):
    b_id = models.CharField(max_length=20)
    b_name = models.CharField(db_index=True,max_length=200)
    b_page = models.IntegerField()
    b_year = models.CharField(max_length=50)
    authors = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)

    def __str__(self):
        return self.b_name
