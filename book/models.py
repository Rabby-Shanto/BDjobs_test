
from django.db import models

# Create your models here.


class Book(models.Model):
    age_choices = [
        ('20','20'),
        ('25','25'),
        ('30','30'),
        ('40','40'),
    ]

    book_type = [
        ('science','Science'),
        ('tech','Tech'),
        ('lifestyle','Lifestyle')
    ]

    serial = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100)
    publisher_age = models.CharField(max_length=20,choices=age_choices,default=0)
    page_no = models.IntegerField(default=0)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100,choices=book_type)

    def __str__(self) -> str:
        return self.title
